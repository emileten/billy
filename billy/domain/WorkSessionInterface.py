import time
import typing
from typing import Union
import pandas as pd

class WorkSessionInterface:

    """
    abstraction for a work session
    """

    def end_session(self) -> None:

        """
        ends this session by adding a field representing the end time.
        """
        pass


    def is_ended(self) -> bool:

        """
        Returns
        -------
        true if this session is done.
        """