from billy.domain import WorkLogInterface.WorkLogInterface


class WorkLogTable(WorkLogInterface):
    """
    abstraction for a work log
    """

    def add_session(self):

        """
        adds a session to this work log.
        """

        pass

    def has_session(self, session : WorkSession):

        """
        check if a session belongs to this log
        """
        raise NotImplementedError
