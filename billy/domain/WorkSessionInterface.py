from typing import Union
import pendulum as pdl


class WorkSessionInterface(object):

    """
    abstraction for a work session
    """

    start_time: pdl.DateTime
    end_time: Union[None, pdl.DateTime]

    def get_start_time(self) -> pdl.DateTime:

        """
        Returns
        -------
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
        the end time of this work session if it's ended.
        """

        raise NotImplementedError
