from src.freebilly.domain.AbstractWorkLog import AbstractWorkLog
from src.freebilly.domain.WorkSessionInterface import WorkSessionInterface
import pendulum as pdl


class WorkLogSet(AbstractWorkLog):

    """
    implementation of AbstractWorkLog using a Set.
    """

    client: str
    project: str
    sessions: set

    def __init__(self, client, project, sessions=set()):
        self.client = client
        self.project = project
        self.sessions = sessions

    def add_session(self, session: WorkSessionInterface):

        self.sessions.add(session)

    def has_session(self, session: WorkSessionInterface):

        return session in self.sessions

    def total_time(self, start_time: pdl.DateTime, end_time: pdl.DateTime) -> int:

        # filter sessions that have their start time after start_time AND end_time before end_time
        total = 0
        for labor in self.sessions:
            if labor.start_time >= start_time and labor.end_time <= end_time:
                total = total + labor.total_time()

