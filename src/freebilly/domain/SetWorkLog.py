from typing import Set
from src.freebilly.domain.AbstractWorkLog import AbstractWorkLog
from src.freebilly.domain.PendulumWorkSession import PendulumWorkSession
import pendulum as pdl


class SetWorkLog(AbstractWorkLog):

    """
    implementation of AbstractWorkLog using a Set and PendulumWorkSession
    @TODO this should work with any AbstractWorkSession. Not just with PendulumWorkSession. This probably requires a separate AbstractWorkTime class.
    """

    __client: str
    __project: str
    __sessions: Set[PendulumWorkSession]

    def __init__(self, client, project, sessions=None) -> None:
        self.__client = client
        self.__project = project
        if sessions is None:
            self.__sessions = set()
        else:
            self.__sessions = sessions

    def add_session(self, session: PendulumWorkSession) -> None:

        if not session.is_ended():
            raise ValueError("cannot record an ongoing work session")
        self.__sessions.add(session)

    def __contains__(self, session: PendulumWorkSession) -> bool:

        return session in self.__sessions

    def total_time(self, start_time: pdl.DateTime, end_time: pdl.DateTime) -> int:

        # filter sessions that have their start time after start_time AND end_time before end_time
        total = 0
        for labor in self.__sessions:
            if (
                labor.get_start_time() >= start_time
                and labor.get_end_time() <= end_time
            ):
                total = total + labor.total_time()
        return total
