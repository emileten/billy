import abc
from src.freebilly.repository.AbstractRepository import AbstractRepository

class AbstractUnitOfWork(abc.ABC):
    """
    object to atomically operate on work log repository.
    While the repository represents the persistence mechanism, the unit of work wraps transactions with the repository. .
    """

    work_logs: AbstractRepository

    def __exit__(self, *args):
        self.rollback()

    @abc.abstractmethod
    def commit(self) -> None:
        """
        operate a change to the repository
        """
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self) -> None:
        """
        Returns
        -------
        AbstractRepository
            the repo it operates on
        """
        raise NotImplementedError