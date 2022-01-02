from typing import Tuple
from freebilly.repository.AbstractUnitOfWork import AbstractUnitOfWork
from freebilly.services.AbstractServiceLayer import AbstractServiceLayer
from freebilly.domain.OrderedSetWorkLog import OrderedSetWorkLog
from freebilly.domain.PendulumWorkSession import PendulumWorkSession

# TODO coupling with OrderedSetWorkLog and PendulumWorkSession


class ConcreteServiceLayer(AbstractServiceLayer):
    @staticmethod
    def start_session(
        uow: AbstractUnitOfWork, client: str, project: str
    ) -> Tuple[OrderedSetWorkLog, PendulumWorkSession]:

        work_session = PendulumWorkSession()
        with uow:
            if uow.work_logs.exists(client, project):
                work_log = uow.work_logs.get(client, project)
            else:
                work_log = OrderedSetWorkLog(client, project)

        return work_log, work_session

    @staticmethod
    def end_session(
        uow: AbstractUnitOfWork,
        work_log: OrderedSetWorkLog,
        work_session: PendulumWorkSession,
    ):

        with uow:
            work_session.end_session()
            work_log.add_session(work_session)
            uow.commit(work_log)
