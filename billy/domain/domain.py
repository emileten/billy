import time
import typing
from typing import Union
import pandas as pd

class WorkSession:
    """
    abstraction for a work session
    """

    client: str
    project: str
    start_time: time.struct_time
    end_time: Union[None, time.struct_time]

    def __init__(self, client: str, project: str) -> None:

        self.client = client
        self.project = project
        self.start_time = time.localtime()

    def end_session(self) -> None:
        """
        adds a field `end_time` of the type `time.struct_time` to this object.
        """
        if self.end_time is not None:
            raise TypeError('this work session was already ended')
        self.end_time = time.localtime()



class Bill:
    """
    abstraction for a bill
    """

    pass
