from pathlib import Path
from src.freebilly.repository.CsvRepository import CsvRepository
from src.freebilly.repository.AbstractUnitOfWork import AbstractUnitOfWork

class CsvUnitOfWork(AbstractUnitOfWork):

    """

    """
    def __init__(self, path: Path):
        self.work_logs = CsvRepository(path=path)

    def commit(self):
        """
        operate on the work log or the work logs.
        """
        raise NotImplementedError

    def rollback(self):

        pass