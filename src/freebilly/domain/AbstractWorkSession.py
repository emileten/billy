from __future__ import annotations
from typing import Any
import abc


class AbstractWorkSession(abc.ABC):

    """
    abstraction for a work session
    """

    @abc.abstractmethod
    def get_start_time(self) -> Any:

        """
        Returns
        -------
        Any
            the start time of this work session
        """

        raise NotImplementedError

    @abc.abstractmethod
    def end_session(self) -> None:

        """
        ends this session by adding a field representing the end time.

        Raises
        ------
        TypeError
            if this session was already ended
        """

        raise NotImplementedError

    @abc.abstractmethod
    def is_ended(self) -> bool:

        """
        Returns
        -------
        bool
            true if this session is done.
        """

        raise NotImplementedError

    @abc.abstractmethod
    def get_end_time(self) -> Any:

        """
        Returns
        -------
        Any
            the end time of this work session if it's ended, None otherwise.
        """

        raise NotImplementedError

    @abc.abstractmethod
    def overlaps(self, other: AbstractWorkSession) -> bool:

        """
        check whether this session overlaps with another in time. Both have to be
        ended.

        Parameters
        ----------
        other : AbstractWorkSession

        Returns
        -------
        bool
            false if the time interval of `self` is entirely outside of the time interval of `other`.

        Raises
        ------
        TypeError
            if `self` or `other` are not ended.
        """

        raise NotImplementedError

    @abc.abstractmethod
    def total_time(self) -> int:

        """
        Returns
        -------
        int
            total time spent working during this session in minutes if it's ended.
        Raises
        ------
        TypeError
            if this session is not ended
        """
