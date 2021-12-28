from pathlib import Path
from src.freebilly.services.AbstractServiceLayer import AbstractServiceLayer
from src.freebilly.domain.OrderedSetWorkLog import OrderedSetWorkLog
from src.freebilly.domain.PendulumWorkSession import PendulumWorkSession

class ConcreteServiceLayer(AbstractServiceLayer):

    def start_session(self, path: Path, client: str, project: str) -> Tuple[
        AbstractRepository, AbstractWorkLog, AbstractWorkSession]:

        repo = CsvRepository(pathlib.Path(path))
        if repo.exists(client, project):
            work_log = repo.get(client, project)
        else:
            work_log = OrderedSetWorkLog(client, project)
        work_session = PendulumWorkSession()
        return repo, work_log, work_session

    def end_session(self, repo: AbstractRepository, work_log: AbstractWorkLog,
                    work_session: AbstractWorkSession) -> None:

        work_session.end_session()
        work_log.add_session(work_session)
        repo.push(work_log)
