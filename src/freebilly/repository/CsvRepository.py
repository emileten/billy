from typing import Union
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

    __work_log_paths: Path
    __work_log_prefix: "work_log"
    __work_log: Union[None, AbstractWorkLog]

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

        raise NotImplementedError

    def exists(self, client: str, project: str) -> bool:

        raise NotImplementedError

    def get(self, client: str, project: str) -> AbstractWorkLog:

        new_work_log = SetWorkLog(client, project) #TODO here is a coupling with SetWorkLog
        with open(str(self.__work_log_path.joinpath(self.__work_log_prefix + "_" + client + "_" + project))) as csv_file:
            for row in csv.DictReader(csv_file, fieldnames=['start_time', 'end_time'], delimiter=' ', quotechar='|'):
                new_work_log.add_session(PendulumWorkSession(pdl.parse(row['start_time']), pdl.parse(row['end_time'])))

        return new_work_log