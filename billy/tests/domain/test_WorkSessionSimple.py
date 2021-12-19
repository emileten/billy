import pendulum as pdl
import pytest
from billy.domain.WorkSessionSimple import WorkSessionSimple

def test_get_start_time():
    my_session = WorkSessionSimple()
    expected = pdl.now()
    actual = my_session.get_start_time()
    assert isinstance(actual, pdl.DateTime)
    assert (
        actual.diff(expected).in_minutes() == 0
    )


def test_is_ended():
    my_session = WorkSessionSimple()
    my_session.end_session()
    assert my_session.is_ended()


def test_get_end_time():
    my_session = WorkSessionSimple().end_session()
    expected = pdl.now()
    actual = my_session.get_end_time()
    assert isinstance(actual, pdl.DateTime)
    assert (
        actual.diff(expected).in_minutes() == 0
    )


def test_end_session():
    assert (
        pdl.now().diff(WorkSessionSimple().end_session().end_time).in_minutes() == 0
    )
    with pytest.raises(TypeError):
        WorkSessionSimple().end_session().end_session()

def test_overlaps():

    s1 = WorkSessionSimple()
    s2 = WorkSessionSimple()
    s1.end_session()
    s2.end_session()
    assert s1.overlaps(s2)
    s1 = WorkSessionSimple().end_session()
    s2 = WorkSessionSimple().end_session()
    assert not s1.overlaps(s2)
