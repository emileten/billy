from billy.domain.WorkLogInterface import WorkLogInterface
from billy.domain.WorkSessionInterface import WorkSessionInterface


class WorkLogDict(WorkLogInterface):

    """
    implementation of WorkLogInterface using a Dict.
    """

    def add_session(self, session: WorkSessionInterface):

        raise NotImplementedError

    def has_session(self, session: WorkSessionInterface):

        raise NotImplementedError

    def total_time(self, start_time: pendulum.DateTime, end_time: pendulum.DateTime):

        raise NotImplementedError
