from pathlib import Path
from src.freebilly.repository.AbstractUnitOfWork import AbstractUnitOfWork
from src.freebilly.services.AbstractServiceLayer import AbstractServiceLayer
from src.freebilly.domain.OrderedSetWorkLog import OrderedSetWorkLog
from src.freebilly.domain.PendulumWorkSession import PendulumWorkSession
#TODO coupling with OrderedSetWorkLog and PendulumWorkSession

class ConcreteServiceLayer(AbstractServiceLayer):

    def start_session(self, uow, client, project):

        work_session = PendulumWorkSession()
        with uow:
            repo = uow.get()
            if repo.exists(client, project):
                work_log = repo.get(client, project)
            else:
                work_log = OrderedSetWorkLog(client, project)
        return repo, work_log, work_session

    def end_session(self, repo, work_log,
                    work_session):

        work_session.end_session()
        work_log.add_session(work_session)
        repo.push(work_log)
