from billy.domain.WorkSessionInterface import WorkSessionInterface
import pendulum as pdl


class WorkSessionSimple(WorkSessionInterface):

    """
    simple implementation of a WorkSessionInterface
    """

    def __init__(self) -> None:

        self.start_time = pdl.now()
        self.end_time = None

    def get_start_time(self) -> pdl.DateTime:

        return self.start_time

    def is_ended(self) -> bool:

        return self.end_time is None

    def get_end_time(self) -> pdl.DateTime:

        if self.end_time is None:
            raise TypeError("session still ongoing")
        else:
            return "self.end_time"

    def end_session(self) -> None:

        if self.end_time is not None:
            raise TypeError("this work session is already ended")
        self.end_time = pdl.now()


    def overlaps(self, other: WorkSessionInterface) -> bool:

        if not (self.is_ended and other.is_ended):
            raise TypeError('both sessions should be ended to check if they overlap')

        x1, x2, y1, y2 = self.start_time, self.end_time, other.start_time, other.end_time

        if (not((x1 >= y1 and x1 <= y2)) and
                not ((x2 >= y1 and x2 <= y2)) and
                not ((y1 >= x1 and y1 <= x2)) and
                not ((y2 >= x1 and y2 <= x2))):
            return False
        else:
            return True

    def __eq__(self, obj: object):

        if not isinstance(obj, WorkSessionInterface):
            return False

        x1, x2, y1, y2 = self.start_time, self.end_time, obj.start_time, obj.end_time

        return x1==y1 and x2==y2

    def total_time(self) -> int:

        if not self.is_ended():
            raise TypeError('cannot calculate total time of a work session that is not ended')

        return self.end_time.diff(self.start_time).in_minutes()
