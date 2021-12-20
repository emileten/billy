from src.freebilly.domain.AbstractWorkLog import AbstractWorkLog
from src.freebilly.domain.AbstractWorkSession import AbstractWorkSession
import pendulum as pdl


class SetWorkLog(AbstractWorkLog):

    """
    implementation of AbstractWorkLog using a Set.
    """

    client: str
    project: str
    sessions: set

    def __init__(self, client, project, sessions=set()) -> None:
        self.client = client
        self.project = project
        self.sessions = sessions

    def add_session(self, session: AbstractWorkSession) -> None:

        self.sessions.add(session)

    def has_session(self, session: AbstractWorkSession) -> bool:

        return session in self.sessions

    def total_time(self, start_time: pdl.DateTime, end_time: pdl.DateTime) -> int:

        # filter sessions that have their start time after start_time AND end_time before end_time
        total = 0
        for labor in self.sessions:
            if labor.start_time >= start_time and labor.end_time <= end_time:
                total = total + labor.total_time()
