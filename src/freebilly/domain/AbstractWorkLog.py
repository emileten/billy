import abc
from typing import Any
from src.freebilly.domain.AbstractWorkSession import AbstractWorkSession


class AbstractWorkLog(abc.ABC):
    """
    abstraction for a work log
    """

    @abc.abstractmethod
    def add_session(self, session: AbstractWorkSession) -> None:

        """
        adds a session to this work log.
        Parameters
        ----------
        session : AbstractWorkSession
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
