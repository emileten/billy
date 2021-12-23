import abc
from typing import Any, Generator
from src.freebilly.domain.AbstractWorkSession import AbstractWorkSession


class AbstractWorkLog(abc.ABC):
    """
    abstraction for a work log
    """

    __client: str
    __project: str

    @abc.abstractmethod
    def add_session(self, session: AbstractWorkSession) -> None:

        """
        adds an ended work session to this work log.
        Parameters
        ----------
        session : AbstractWorkSession

        Raises
        ------
        ValueError
            if session is not ended.
        """

        raise NotImplementedError

    @abc.abstractmethod
    def total_time(self, start_time: Any, end_time: Any) -> int:

        """
        returns the total time in minutes spent working between specified moments in the time
        interval spanned by this work log.

        Parameters
        ----------
        start_time
        end_time

        Returns
        -------
        int
        """

        raise NotImplementedError

    @abc.abstractmethod
    def __contains__(self, session: AbstractWorkSession) -> bool:

        """
        Parameters
        ----------
        session : AbstractWorkSession

        Returns
        -------
        bool
            true if this session is contained in this log as per the equality definition.
        """

        raise NotImplementedError

    @abc.abstractmethod
    def get_client(self) -> str:

        """
        Returns
        -------
        str
            this work log's client
        """

        raise NotImplementedError

    @abc.abstractmethod
    def get_project(self) -> str:
        """
        Returns
        -------
        str
            this work log's project
        """

        raise NotImplementedError

    @abc.abstractmethod
    def is_empty(self) -> bool:

        """
        Returns
        -------
        bool
            True if this work log contains no work sessions.

        """

        raise NotImplementedError

    @abc.abstractmethod
    def get_work_sessions(self) -> Generator[AbstractWorkSession, None, None]:

        """
        Yields
        -------
            AbstractWorkSession
        """