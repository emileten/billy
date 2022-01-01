from tempfile import TemporaryDirectory
from pathlib import Path
import pytest
import pendulum as pdl
from src.freebilly.repository.CsvUnitOfWork import CsvUnitOfWork
from src.freebilly.services.ConcreteServiceLayer import ConcreteServiceLayer
from src.freebilly.domain.PendulumWorkSession import PendulumWorkSession
from src.freebilly.domain.OrderedSetWorkLog import OrderedSetWorkLog


def test_start_session():

    with TemporaryDirectory() as fake_dir_path:
        uow = CsvUnitOfWork(Path(fake_dir_path))
        work_log, work_session = ConcreteServiceLayer.start_session(
            uow=uow, client="A", project="1"
        )
        assert work_session.get_start_time().diff(pdl.now()).in_minutes() == 0
        assert not work_session.is_ended()
        assert work_log.is_empty()  # because we have no data in this tempdir !


def test_end_session():

    with TemporaryDirectory() as fake_dir_path:
        uow = CsvUnitOfWork(Path(fake_dir_path))
        ongoing_session = PendulumWorkSession(
            start_time=pdl.datetime(1, 1, 1)
        )
        yet_empty_work_log = OrderedSetWorkLog(client="A", project="1")
        ConcreteServiceLayer.end_session(
            uow=uow, work_log=yet_empty_work_log, work_session=ongoing_session
        )
        assert uow.work_logs.exists(client="A", project="1")
        assert uow.work_logs.valid(client="A", project="1")
        assert ongoing_session in uow.work_logs.get(client="A", project="1")
