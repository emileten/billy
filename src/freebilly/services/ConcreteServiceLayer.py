from typing import Tuple
from src.freebilly.repository.AbstractUnitOfWork import AbstractUnitOfWork
from src.freebilly.services.AbstractServiceLayer import AbstractServiceLayer
from src.freebilly.domain.OrderedSetWorkLog import OrderedSetWorkLog
from src.freebilly.domain.PendulumWorkSession import PendulumWorkSession

# TODO coupling with OrderedSetWorkLog and PendulumWorkSession


class ConcreteServiceLayer(AbstractServiceLayer):
    def start_session(
        self, uow: AbstractUnitOfWork, client: str, project: str
    ) -> Tuple[OrderedSetWorkLog, PendulumWorkSession]:

        work_session = PendulumWorkSession()
        with uow:
            if uow.work_logs.exists(client, project):
                work_log = uow.work_logs.get(client, project)
            else:
                work_log = OrderedSetWorkLog(client, project)

        return work_log, work_session

    def end_session(
        self,
        uow: AbstractUnitOfWork,
        work_log: OrderedSetWorkLog,
        work_session: PendulumWorkSession,
    ):

        with uow:
            work_session.end_session()
            work_log.add_session(work_session)
            uow.commit(work_log)
