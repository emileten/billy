from billy.domain.WorkLogInterface import WorkLogInterface
from billy.domain.WorkSessionInterface import WorkSessionInterface


class WorkLogTable(WorkLogInterface):
    """
    abstraction for a work log
    """

    def add_session(self, sess):

        """
        adds a session to this work log.
        """

        pass

    def has_session(self, session : WorkSessionInterface):

        """
        check if a session belongs to this log
        """
        raise NotImplementedError
