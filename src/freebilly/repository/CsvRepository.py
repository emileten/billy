from typing import Union, List
from pathlib import Path
import csv
from src.freebilly.repository.AbstractRepository import AbstractRepository
from src.freebilly.domain.AbstractWorkLog import AbstractWorkLog
from src.freebilly.domain.SetWorkLog import SetWorkLog
from src.freebilly.domain.PendulumWorkSession import PendulumWorkSession
import pendulum as pdl #TODO this is coupled with pendulum so Pendulum WorkSession...

class CsvRepository(AbstractRepository):

    """
    essentially, operates to and from a work log, to and from a csv file where a row is
    a work session in that work log, with a start time and an end_time column.
    """

    __work_log_path: Path
    __work_log_prefix: "work_log"
    __work_log: Union[None, AbstractWorkLog]
    __field_names = ['start_time', 'end_time']

    def __init__(self, path: Path) -> None:

        """
        Parameters
        ----------
        path: Path
            Path.exists() should return True
        """
        if not path.exists():
            raise ValueError("nonexistent path")
        self.__work_log_path = path
        self._work_log = None


    def push(self, work_log: AbstractWorkLog) -> None:

        with open(self.get_csv_file_path(work_log.get_client(), work_log.get_project()), 'w', newline='') as csvfile:
            work_log_writer = csv.DictWriter(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL, self.__field_names)
            work_log_writer.writeheader()
            for work_session in work_log:
                work_log_writer.writerow({'start_time': work_session.get_start_time(), 'end_time': work_session.get_end_time()})

    def exists(self, client: str, project: str) -> bool:

        return Path(self.get_csv_file_path(client, project)).exists()

    def get(self, client: str, project: str) -> AbstractWorkLog:

        csv_file_path = self.get_csv_file_path(client, project)
        if not self.exists(client, project)
            raise ValueError(f'file for client {client} and project {project} does not exist')
        new_work_log = SetWorkLog(client, project) #TODO here is a coupling with SetWorkLog
        with open(csv_file_path) as csv_file:
            for row in csv.DictReader(csv_file, fieldnames=['start_time', 'end_time'], delimiter=' ', quotechar='|'):
                new_work_log.add_session(PendulumWorkSession(pdl.parse(row['start_time']), pdl.parse(row['end_time'])))

        return new_work_log

    def get_csv_file_path(self, client: str, project: str) -> Path:

        """

        Parameters
        ----------
        client: str
        project: str

        Returns
        -------
        Path
            full path to csv file containing that work log
        """

        return str(self.__work_log_path.joinpath(self.__work_log_prefix + "_" + client + "_" + project + ".csv"))
