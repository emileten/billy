import pendulum as pdl
import pytest
from src.freebilly.domain.PendulumWorkSession import PendulumWorkSession

# TODO many tests here are contingent on machine execution time


def test_get_start_time():
    my_session = PendulumWorkSession()
    expected = pdl.now()
    actual = my_session.get_start_time()
    assert isinstance(actual, pdl.DateTime)
    assert actual.diff(expected).in_minutes() == 0


def test_is_ended():
    my_session = PendulumWorkSession().end_session()
    assert my_session.is_ended()


def test_get_end_time():
    my_session = PendulumWorkSession().end_session()
    expected = pdl.now()
    actual = my_session.get_end_time()
    assert isinstance(actual, pdl.DateTime)
    assert actual.diff(expected).in_minutes() == 0


def test_end_session():
    my_session = PendulumWorkSession().end_session()
    assert pdl.now().diff(my_session.get_end_time()).in_minutes() == 0
    with pytest.raises(TypeError):
        my_session.end_session()


def test_overlaps():

    s1 = PendulumWorkSession()
    s2 = PendulumWorkSession()
    assert s1.end_session().overlaps(s2.end_session())
    assert (
        not PendulumWorkSession()
        .end_session()
        .overlaps(PendulumWorkSession().end_session())
    )


def test_unequal():

    o1 = PendulumWorkSession()
    o2 = "str"
    assert o1 != o2
    o1 = PendulumWorkSession().end_session()
    o2 = PendulumWorkSession().end_session()
    assert o1 != o2


def test_total_time():

    o1 = PendulumWorkSession().end_session()
    assert o1.total_time() == 0
