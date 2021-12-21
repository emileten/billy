import abc
from src.freebilly.domain.AbstractWorkLog import AbstractWorkLog


class AbstractRepository(abc.ABC):

    """
    abstraction for a repository
    """

    @abc.abstractmethod
    def read(self) -> AbstractWorkLog:

        """
        retrieve data from external storage and return a Work Log.

        Returns
        -------

        """

    @abc.abstractmethod
    def write(self):

        """
        expand

        Returns
        -------

        """
