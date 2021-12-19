from src.billy.domain.WorkSessionSimple import WorkSessionSimple
from src.billy.domain.WorkLogSet import WorkLogSet
import pendulum as pdl

def test_add_session():

    mySession = WorkSessionSimple()
    myLog = WorkLogSet(client="A", project="1")
    myLog.add_session(mySession)
    assert mySession in myLog


def test_has_session():

    mySession = WorkSessionSimple()
    myLog = WorkLogSet(client="A", project="1", sessions=set(mySession))
    assert mySession in myLog


def test_total_time():

    start = pdl.now()
    myLog = WorkLogSet(client="A", project="1", sessions=set())
    myLog.add_session(WorkSessionSimple().end_session())
    myLog.add_session(WorkSessionSimple().end_session())
    end = pdl.now()
    assert myLog.total_time(start, end) == 0
