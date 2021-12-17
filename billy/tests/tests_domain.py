import time
import pytest
from billy import domain


def test_start_session_time():
    """
    tests that billy.WorkSession.__init__ assigns a correct value to a start time field.
    """
    assert (
        time.localtime() == domain.WorkSession(client="B", project="P").start_time
    )  # hopefully fast enough to catch the time !


def test_end_session_time():
    """
    tests that the method billy.WorkSession.end_session_time object assigns correct start time.
    """
    assert (
        time.localtime()
        == domain.WorkSession(client="B", project="P").end_session().end_time
    )

    with pytest.raises(TypeError):
        domain.WorkSession(client="B", project="P").end_session().end_session()


def test_add_session():
    """
    tests that you can add a billy.WorkSession to a billy.WorkLog
    """

    mySession = domain.WorkSession(client="B", project="P")
    myLog = domain.WorkLog(client="B")
    myLog.add_session(mySession)
    assert mySession in myLog
