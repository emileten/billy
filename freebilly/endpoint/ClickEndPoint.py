import logging
from pathlib import Path
from freebilly.endpoint.AbstractEndPoint import AbstractEndPoint
from freebilly.services.ConcreteServiceLayer import ConcreteServiceLayer
from freebilly.repository.CsvUnitOfWork import CsvUnitOfWork
import logging
import click

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class ClickEndPoint(AbstractEndPoint):

    @click.group()
    @click.option('--debug/--no-debug', default=False)
    def freebilly_cli(debug):
        if debug:
            logging.root.setLevel(logging.DEBUG)

    @freebilly_cli.command(help="record a work session in a log")
    @click.option(
        "--path",
        required=True,
        help="path to the folder where the work log is stored or is to be stored",
    )
    @click.option(
        "--client", required=True, help="client with whom you're working",
    )
    @click.option(
        "--project", required=True, help="project on which you're working",
    )
    def record_session(path: str, client: str, project: str) -> None:

        logging.info(f"started session for client {client } and project {project}")
        uow = CsvUnitOfWork(Path(path))
        work_log, work_session = ConcreteServiceLayer.start_session(
            uow, client, project
        )
        click.confirm("press enter to end the session...")
        logging.info("ending session and pushing to work log...")
        ConcreteServiceLayer.end_session(uow, work_log, work_session)
