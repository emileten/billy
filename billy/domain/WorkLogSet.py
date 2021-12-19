from billy.domain.WorkLogInterface import WorkLogInterface
from billy.domain.WorkSessionInterface import WorkSessionInterface
import pendulum as pdl

class WorkLogSet(WorkLogInterface):

    """
    implementation of WorkLogInterface using a Dict.
    """

    client: str
    project: str
    sessions: set

    def __init__(self, client, project, sessions=set()):
        self.client = client
        self.project = project
        self.sessions = sessions

    def add_session(self, session: WorkSessionInterface):

        raise NotImplementedError

    def has_session(self, session: WorkSessionInterface):

        raise NotImplementedError

    def total_time(self, start_time: pdl.DateTime, end_time: pdl.DateTime):

        raise NotImplementedError
