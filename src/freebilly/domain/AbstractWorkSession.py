from __future__ import annotations
from typing import Union
import pendulum as pdl


class AbstractWorkSession(object):

    """
    abstraction for a work session
    """

    start_time: pdl.DateTime
    end_time: Union[None, pdl.DateTime]

    def get_start_time(self) -> pdl.DateTime:

        """
        Returns
        -------
        pdl.DateTime
            the start time of this work session
        """

        raise NotImplementedError

    def end_session(self) -> None:

        """
        ends this session by adding a field representing the end time.

        Raises
        ------
        TypeError
            if this session was already ended
        """

        raise NotImplementedError

    def is_ended(self) -> bool:

        """
        Returns
        -------
        bool
            true if this session is done.
        """

        raise NotImplementedError

    def get_end_time(self) -> pdl.DateTime:

        """
        Raises
        ------
        TypeError
            if this session is not yet ended.
        Returns
        -------
        pdl.DateTime
            the end time of this work session if it's ended.
        """

        raise NotImplementedError

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
