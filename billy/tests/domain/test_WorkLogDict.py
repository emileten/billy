from billy.domain.WorkLogDict import WorkLogDict


def test_add_session():
    """
    tests that you can add WorkSessionSimple to a WorkLogDict
    """

    mySession = WorkSessionSimple(client="B", project="P")
    myLog = domain.WorkLogTable.WorkLogTable(client="B")
    myLog.add_session(mySession)
    assert mySession in myLog
