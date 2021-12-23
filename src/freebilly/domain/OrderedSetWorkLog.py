from typing import Set, Union, Generator
from ordered_set import OrderedSet
from src.freebilly.domain.AbstractWorkLog import AbstractWorkLog
from src.freebilly.domain.PendulumWorkSession import PendulumWorkSession
import pendulum as pdl


class OrderedSetWorkLog(AbstractWorkLog):

    """
    implementation of AbstractWorkLog using a Set and PendulumWorkSession
    @TODO this is coupled to PendulumWorkSession. Can couple that to AbstractWorkSession instead ?
    """

    __client: str
    __project: str
    __sessions: OrderedSet[PendulumWorkSession]

    def __init__(self, client: str, project: str, sessions : Union[None, OrderedSet[PendulumWorkSession]] = None) -> None:
        self.__client = client
        self.__project = project
        self.__sessions = OrderedSet()
        if sessions is not None:
            for work_session in sessions:
                self.add_session(work_session)

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

    def get_client(self) -> str:

        return self.__client

    def get_project(self) -> str:

        return self.__project

    def is_empty(self) -> bool:

        return len(self.__sessions) == 0

    def get_work_sessions(self) -> Generator[PendulumWorkSession, None, None]:

        for s in self.__sessions:
            yield s