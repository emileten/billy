class WorkSession:
    """
    abstraction for a work session
    """
    def __init__(self):

        """
        adds a field `start_time` indicating local time. of the type `time.struct_time` to this object.
        """

        raise NotImplementedError

    def end_session(self):

        """
        adds a field `end_time` of the type `time.struct_time` to this object.
        """

        raise NotImplementedError


class WorkLog:
    """
    abstraction for a work log
    """
    def add_session(self):

        """
        adds a session to this work log.
        """

        raise NotImplementedError

    def __contains__(self, session):

        """
        check if a session belongs to this log
        """
        raise NotImplementedError

class Bill:
    """
    abstraction for a bill
    """

    pass