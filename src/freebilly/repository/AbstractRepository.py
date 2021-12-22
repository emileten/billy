import abc
from typing import Union
from src.freebilly.domain.AbstractWorkLog import AbstractWorkLog


class AbstractRepository(abc.ABC):

    """
    abstraction for a work log repository
    """

    __work_log: Union[None, AbstractWorkLog]

    @abc.abstractmethod
    def push(self, work_log: AbstractWorkLog) -> None:

        """
        pushes work log to repository

        Parameters
        ----------
        work_log: AbstractWorkLog
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
            True if a work log associated with `client` and `project` can be fetched
            from repo.
        """

        raise NotImplementedError

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
            if work log specified does not exist.
        """

        raise NotImplementedError
