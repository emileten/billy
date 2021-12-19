from billy.domain.WorkSessionSimple import WorkSessionSimple
from billy.domain.WorkLogDict import WorkLogDict

def test_add_session():

    mySession = WorkSessionSimple()
    myLog = WorkLogDict(client='A', project='1')
    myLog.add_session(mySession)
    assert


def test_has_session():

    mySession = WorkSessionSimple()
    myLog = WorkLogDict(client='A', project='1', {'mySession' : mySession})
    myLog.add_session(mySession)
    assert


    def test_total_time():
    assert False
