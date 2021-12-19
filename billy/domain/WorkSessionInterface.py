import typing
import pendulum


class WorkSessionInterface(object):

    """
    abstraction for a work session
    """

    start_time: pendulum.DateTime
    end_time: Union[None, pendulum.DateTime]

    def get_start_time(self) -> pendulum.DateTime:

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

    def get_end_time(self) -> pendulum.DateTime:

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
