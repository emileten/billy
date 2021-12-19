from src.billy.domain.WorkSessionInterface import WorkSessionInterface
import pendulum as pdl


class WorkLogInterface(object):
    """
    abstraction for a work log
    """

    def add_session(self, session: WorkSessionInterface) -> None:

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

    def __contains__(self, item: WorkSessionInterface) -> bool:

        """
        Parameters
        ----------
        item : WorkSessionInterface

        Returns
        -------
        true if this session is contained in this log as per the equality definition.
        """

        raise NotImplementedError
