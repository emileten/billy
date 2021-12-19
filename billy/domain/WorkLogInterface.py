from billy.domain.WorkSessionInterface import WorkSessionInterface
import pendulum


class WorkLogInterface:
    """
    abstraction for a work log
    """

    def add_session(self, session: WorkSessionInterface):

        """
        adds a session to this work log.
        """

        pass

    def has_session(self, session: WorkSessionInterface):

        """
        check if a session belongs to this log
        """
        raise NotImplementedError

    def total_time(self, start_time: pendulum.DateTime, end_time: pendulum.DateTime):

        """
        returns the total time spent working between specified moments in time.
        """
