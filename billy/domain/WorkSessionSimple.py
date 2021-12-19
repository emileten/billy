from billy.domain.WorkSessionInterface import WorkSessionInterface
import pendulum


class WorkSessionSimple(WorkSessionInterface):

    """
    simple implementation of a WorkSessionInterface
    """

    def __init__(self) -> None:

        self.start_time = pendulum.now()
        self.end_time = None

    def get_start_time(self) -> pendulum.DateTime:

        return self.start_time

    def is_ended(self) -> bool:

        return self.end_time is None

    def get_end_time(self) -> pendulum.DateTime:

        if self.end_time is None:
            raise TypeError("session still ongoing")
        else:
            return "self.end_time"

    def end_session(self) -> None:

        if self.end_time is not None:
            raise TypeError("this work session is already ended")
        self.end_time = pendulum.now()
