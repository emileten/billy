from typing import Union, List
from pathlib import Path
import csv
import logging
from src.freebilly.repository.AbstractRepository import AbstractRepository
from src.freebilly.domain.AbstractWorkLog import AbstractWorkLog
from src.freebilly.domain.OrderedSetWorkLog import OrderedSetWorkLog
from src.freebilly.domain.PendulumWorkSession import PendulumWorkSession
import pendulum as pdl  # TODO this is coupled with pendulum so PendulumWorkSession...


class CsvRepository(AbstractRepository):

    """
    essentially, operates to and from a work log, to and from a csv file where a row is
    a work session in that work log, with a start time and an end_time column.
    """

    __work_log_path: Path
    __work_log_prefix: str
    __work_log: Union[None, AbstractWorkLog]
    __field_names: List

    def __init__(self, path: Path, prefix = "work_log", field_names = ["start_time", "end_time"] ) -> None:

        """
        Parameters
        ----------
        path: Path
            Path.exists() should return True
        """
        if not path.exists():
            raise ValueError("nonexistent path")
        self.__work_log_path = path
        self.__work_log = None
        self.__work_log_prefix = prefix
        self.__field_names = field_names

    def push(self, work_log: AbstractWorkLog) -> None:

        if work_log.is_empty():
            raise ValueError("cannot push an empty work log to repository")
        with open(
            self.get_csv_file_path(work_log.get_client(), work_log.get_project()),
            "w",
            newline="",
        ) as csv_file:
            work_log_writer = csv.DictWriter(
                csv_file,
                fieldnames=self.__field_names,
            )
            work_log_writer.writeheader()
            for work_session in work_log.get_work_sessions():
                work_log_writer.writerow(
                    {
                        "start_time": work_session.get_start_time().to_iso8601_string(),
                        "end_time": work_session.get_end_time().to_iso8601_string(),
                    }
                )

    def exists(self, client: str, project: str) -> bool:

        return Path(self.get_csv_file_path(client, project)).exists()

    def valid(self, client: str, project: str) -> bool:
        """
        assumes the file is valid. walks through it until the second line included
        checking the first row is the right header and the second had parsable data.
        TODO coupling with pendulum here.

        Parameters
        ----------
        client: str
        project: str

        Returns
        -------
        If there is a failure in the first or second line or if it couldn't reach two lines,
        returns False, True otherwise.
        """
        if not self.exists(client, project):
            raise ValueError("cannot check validity of work log that does not exist in repository")
        i = 0
        is_valid = True
        with open(self.get_csv_file_path(client, project), newline="") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if i == 0:
                    if row != ['start_time', 'end_time']:
                        logging.warning("invalid header in csv work log file")
                        is_valid = False
                elif i == 1:
                    try:
                        (pdl.parse(row[0]), pdl.parse(row[1])) # TODO here is a coupling with PendulumWorkSession
                    except Exception:
                        logging.warning("unable to parse first row after header in csv work log file")
                        is_valid = False
                else:
                    break
                i = i + 1
        if i < 2:
            is_valid = False
        return is_valid

    def get(self, client: str, project: str) -> AbstractWorkLog:

        csv_file_path = self.get_csv_file_path(client, project)
        if not self.exists(client, project):
            raise ValueError(
                f"file for client {client} and project {project} does not exist"
            )
        if not self.valid(client, project):
            raise ValueError(
                f"representation of work log in file for client {client} and project {project} is not valid"
            )
        new_work_log = OrderedSetWorkLog(
            client, project
        )  # TODO here is a coupling with OrderedSetWorkLog
        with open(csv_file_path, newline="") as csv_file:
            csv_reader = csv.DictReader(
                csv_file,
                fieldnames=["start_time", "end_time"],
            )
            next(csv_reader) # skip header
            for row in csv_reader:
                new_work_log.add_session(
                    PendulumWorkSession( #TODO here is a coupling with PendulumWorkSession
                        pdl.parse(row["start_time"]), pdl.parse(row["end_time"])
                    )
                )

        return new_work_log

    def get_csv_file_path(self, client: str, project: str) -> str:

        """

        Parameters
        ----------
        client: str
        project: str

        Returns
        -------
        str
            full path to csv file containing that work log
        """

        return str(
            self.__work_log_path.joinpath(
                self.__work_log_prefix + "_" + client + "_" + project + ".csv"
            )
        )
