import logging
import os
from pathlib import Path
import rumps
from freebilly.services.ConcreteServiceLayer import ConcreteServiceLayer as Services
from freebilly.repository.CsvWorkLogUnitOfWork import CsvWorkLogUnitOfWork as UnitOfWork

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class FreeBillyRumpsApp(rumps.App):
    def __init__(self):
        super(FreeBillyRumpsApp, self).__init__(
            "work tracker app", menu=["Start", "End"]
        )
        self.uow = None
        self.work_log = None
        self.work_session = None
        self.path, self.client, self.project = (
            os.getenv("FREEBILLY_PATH"),
            os.getenv("FREEBILLY_CLIENT"),
            os.getenv("FREEBILLY_PROJECT"),
        )
        if self.path is None or self.client is None or self.project is None:
            logging.error(
                "you should set the path, client and project environment variables ot run this app"
            )
            raise ValueError

    @rumps.clicked("Start")
    def start(self, _):

        # For now hard coded... need to find a way...
        self.uow = UnitOfWork(Path(self.path))
        self.work_log, self.work_session = Services.start_session(
            self.uow, self.client, self.project
        )
        rumps.notification(
            "Notification",
            "started work session",
            f"start time : {self.work_session.get_start_time()}",
        )

    @rumps.clicked("End")
    def end(self, _):

        if self.uow is None or self.work_log is None or self.work_session is None:
            rumps.notification(
                "Error",
                "You haven't started a session yet !",
                "Click on 'start' in order to do so",
            )
        else:
            Services.end_session(self.uow, self.work_log, self.work_session)
            rumps.notification(
                "Notification",
                "ended work session",
                f"end time: {self.work_session.get_end_time()}",
            )
            self.uow, self.work_log, self.work_session = None, None, None


if __name__ == "__main__":
    app = FreeBillyRumpsApp()
    app.run()
