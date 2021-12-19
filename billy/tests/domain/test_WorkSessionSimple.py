import pendulum
import pytest
from billy.domain.WorkSessionSimple import WorkSessionSimple


def test_start_session_time():
    assert (
        pendulum.now().diff(WorkSessionSimple()).in_minutes == 0
    )  # hopefully fast enough to catch the time !


def test_end_session_time():
    assert (
        pendulum.now().diff(WorkSessionSimple().end_session().end_time).in_minutes == 0
    )


def test_end_twice_session_time_raises():
    with pytest.raises(TypeError):
        WorkSessionSimple().end_session().end_session()
