from billy.domain.WorkSessionSimple import WorkSessionSimple
from billy.domain.WorkLogSet import WorkLogSet

def test_add_session():

    mySession = WorkSessionSimple()
    myLog = WorkLogSet()
    myLog.add_session(mySession)
    assert mySession in myLog


def test_has_session():

    mySession = WorkSessionSimple()
    myLog = WorkLogSet(client='A', project='1', set([mySession]))
    assert mySession in myLog

def test_total_time():

    myLog = WorkLogSet(client='A', project='1', set())
    myLog.add_session(WorkSessionSimple().end_session())
    myLog.add_session(WorkSessionSimple().end_session())
    assert myLog.total_time()==0
