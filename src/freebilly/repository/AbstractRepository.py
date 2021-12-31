import abc
from src.freebilly.domain.AbstractWorkLog import AbstractWorkLog


class AbstractRepository(abc.ABC):

    """
    abstraction for a repository of work logs
    """

    @abc.abstractmethod
    def push(self, work_log: AbstractWorkLog) -> None:

        """
        pushes a non empty work log to repository.

        Parameters
        ----------
        work_log: AbstractWorkLog

        Raises
        ------
        ValueError
            if `work_log` is empty.
        """

        raise NotImplementedError

    @abc.abstractmethod
    def exists(self, client: str, project: str) -> bool:
        """
        Parameters
        ----------
        client: str
        project: str

        Returns
        -------
        bool
            True if the representation of the work log associated with `client` and `project` can be fetched
            from repo.
        """

        raise NotImplementedError

    @abc.abstractmethod
    def valid(self, client: str, project: str) -> bool:

        """

        Parameters
        ----------
        client: str
        project: str

        Returns
        -------
        bool
            True if the representation of the work log associated with `client` and `project`
            is valid. What 'valid' means depends on the particular implementation of `AbstractRepository`.

        """

    @abc.abstractmethod
    def get(self, client: str, project: str) -> AbstractWorkLog:

        """
        retrieves work log from repository.

        Parameters
        ----------
        client: str
        project: srt

        Returns
        -------
        AbstractWorkLog
            work log, in-memory

        Raises
        ------
        ValueError
            if work log specified does not exist or if, if it exists but
            work log representation is invalid as per `self.valid()`.
        """

        raise NotImplementedError
