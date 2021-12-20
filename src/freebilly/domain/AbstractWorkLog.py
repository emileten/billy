from src.freebilly.domain.AbstractWorkSession import AbstractWorkSession
import pendulum as pdl


class AbstractWorkLog(object):
    """
    abstraction for a work log
    """

    def add_session(self, session: AbstractWorkSession) -> None:

        """
        adds a session to this work log.
        """

        raise NotImplementedError

    def total_time(self, start_time: pdl.DateTime, end_time: pdl.DateTime) -> int:

        """
        returns the total time in minutes spent working between specified moments in the time
        interval spanned by this work log.
        """

        raise NotImplementedError

    def __contains__(self, item: AbstractWorkSession) -> bool:

        """
        Parameters
        ----------
        item : AbstractWorkSession

        Returns
        -------
        true if this session is contained in this log as per the equality definition.
        """

        raise NotImplementedError
