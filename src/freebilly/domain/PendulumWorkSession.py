from typing import Union
from src.freebilly.domain.AbstractWorkSession import AbstractWorkSession
import pendulum as pdl


class PendulumWorkSession(AbstractWorkSession):

    """
    Implementation of an AbstractWorkSession using pendulum.
    """
    __start_time: pdl.DateTime
    __end_time: Union[None, pdl.DateTime]

    def __init__(self) -> None:

        self.__start_time = pdl.now()
        self.__end_time = None

    def get_start_time(self) -> pdl.DateTime:

        return self.__start_time

    def get_end_time(self) -> pdl.DateTime:

        return self.__end_time


    def end_session(self) -> None:

        if self.get_end_time() is not None:
            raise TypeError("this work session is already ended")
        self.__end_time = pdl.now()


    def is_ended(self) -> bool:

        return self.get_end_time() is not None


    def overlaps(self, other: AbstractWorkSession) -> bool:

        if not (self.is_ended() and other.is_ended()):
            raise TypeError("both sessions should be ended to check if they overlap")

        x1, x2, y1, y2 = (
            self.get_start_time(),
            self.get_end_time(),
            other.get_start_time(),
            other.get_end_time(),
        )

        if (
            not (y1 <= x1 <= y2)
            and not (y1 <= x2 <= y2)
            and not (x1 <= y1 <= x2)
            and not (x1 <= y2 <= x2)
        ):
            return False
        else:
            return True

    def __eq__(self, obj: object):

        if not isinstance(obj, PendulumWorkSession):
            return False

        x1, x2, y1, y2 = self.get_start_time(), self.get_end_time(), obj.get_start_time(), obj.get_end_time()

        return x1 == y1 and x2 == y2

    def total_time(self) -> int:

        if not self.is_ended():
            raise TypeError(
                "cannot calculate total time of a work session that is not ended"
            )

        return self.get_end_time().diff(self.get_start_time()).in_minutes()
