import abc
from src.freebilly.repository.AbstractRepository import AbstractRepository
from src.freebilly.domain.AbstractWorkLog import AbstractWorkLog


class AbstractUnitOfWork(abc.ABC):
    """
    an interface to access to a repository object and safely commit changes to database
    """

    work_logs: AbstractRepository

    def __exit__(self, *args):
        self.rollback()

    @abc.abstractmethod
    def commit(self, work_log: AbstractWorkLog) -> None:
        """
        operate a change to the repository
        """
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError
