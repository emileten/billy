import pytest
import pendulum as pdl
from src.freebilly.domain.PendulumWorkSession import PendulumWorkSession
from src.freebilly.domain.SetWorkLog import SetWorkLog


def test_add_session():

    my_session = PendulumWorkSession()
    my_log = SetWorkLog(client="A", project="1")
    with pytest.raises(ValueError):
        my_log.add_session(my_session)
    my_session.end_session()
    my_log.add_session(my_session)
    assert my_session in my_log


def test_has_session():

    my_session = PendulumWorkSession()
    my_log = SetWorkLog(client="A", project="1", sessions=set([my_session]))
    assert my_session in my_log


def test_total_time():

    start = pdl.now()
    my_log = SetWorkLog(client="A", project="1", sessions=set())
    my_log.add_session(PendulumWorkSession().end_session())
    my_log.add_session(PendulumWorkSession().end_session())
    end = pdl.now()
    assert my_log.total_time(start, end) == 0
