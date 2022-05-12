import logging
import os
from pathlib import Path
import subprocess
import re
import rumps
from freebilly.services.ConcreteServiceLayer import ConcreteServiceLayer as Services
from freebilly.repository.CsvWorkLogUnitOfWork import CsvWorkLogUnitOfWork as UnitOfWork

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

PATH = os.getenv("FREEBILLY_PATH")
CLIENT = os.getenv("FREEBILLY_CLIENT")
PROJECT = os.getenv("FREEBILLY_PROJECT")

SHUT_DOWN_WHILE_SLEEPING = False
POWER_MGMT_RE = re.compile(r"IOPowerManagement.*{(.*)}")


def macbook_is_sleeping():
    output = subprocess.check_output(
        "ioreg -w 0 -c IODisplayWrangler -r IODisplayWrangler".split()
    )
    status = POWER_MGMT_RE.search(output.decode("utf-8")).group(1)
    return (
        dict((k[1:-1], v) for (k, v) in (x.split("=") for x in status.split(",")))[
            "DevicePowerState"
        ]
        != "4"
    )


class FreeBillyRumpsApp(rumps.App):
    def __init__(self):
        super(FreeBillyRumpsApp, self).__init__(
            "work tracker app", menu=["Start", "End"]
        )
        self.uow = None
        self.work_log = None
        self.work_session = None
        self.path, self.client, self.project = (
            PATH,
            CLIENT,
            PROJECT,
        )
        if self.path is None or self.client is None or self.project is None:
            logging.error(
                "you should set the path, client and project environment variables ot run this app"
            )
            raise ValueError

    def _ongoing(self):
        return (
            self.uow is not None
            and self.work_log is not None
            and self.work_session is not None
        )

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

        if not self._ongoing():
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

    @rumps.timer(5)
    def _check_status(self, _):
        if macbook_is_sleeping() and self._ongoing():
            logger.info(
                "macbook is sleeping, ending the session"
            )  # can't get notifs to work in a no clicked decorator function :/
            Services.end_session(
                self.uow, self.work_log, self.work_session
            )  # copy pasted that from above b/c doesn't work when externalized in a function.
            self.uow, self.work_log, self.work_session = None, None, None

    # TODO figure out how to send a notif from a non click function.
    # TODO : a timer that catches work activity (e.g. opening slack...) and sends notif to offer start
    # TODO handle shut down as well to end session


if __name__ == "__main__":
    app = FreeBillyRumpsApp()
    app.run()
