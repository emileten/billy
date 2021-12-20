from typing import Set
from src.freebilly.domain.AbstractWorkLog import AbstractWorkLog
from src.freebilly.domain.PendulumWorkSession import PendulumWorkSession
import pendulum as pdl


class SetWorkLog(AbstractWorkLog):

    """
    implementation of AbstractWorkLog using a Set and PendulumWorkSession
    @TODO this should work with any AbstractWorkSession. Not just with PendulumWorkSession. This probably requires a separate AbstractWorkTime class.
    """

    client: str
    project: str
    sessions: Set[PendulumWorkSession]

    def __init__(self, client, project, sessions=None) -> None:
        self.client = client
        self.project = project
        if sessions is None:
            self.sessions = set()
        else:
            self.sessions = sessions

    def add_session(self, session: PendulumWorkSession) -> None:

        self.sessions.add(session)

    def __contains__(self, session: PendulumWorkSession) -> bool:

        return session in self.sessions

    def total_time(self, start_time: pdl.DateTime, end_time: pdl.DateTime) -> int:

        # filter sessions that have their start time after start_time AND end_time before end_time
        total = 0
        for labor in self.sessions:
            if (
                labor.get_start_time() >= start_time
                and labor.get_end_time() <= end_time
            ):
                total = total + labor.total_time()
        return total
