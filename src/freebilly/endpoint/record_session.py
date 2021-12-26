from src.freebilly.domain.PendulumWorkSession import PendulumWorkSession
from src.freebilly.domain.OrderedSetWorkLog import OrderedSetWorkLog
from src.freebilly.repository.CsvRepository import CsvRepository
import sys
import logging
import pathlib

logging.basicConfig(level=logging.INFO)
path, client, project = (sys.argv[1], sys.argv[2], sys.argv[3])
repo = CsvRepository(pathlib.Path(path))
if repo.exists(client, project):
    work_log = repo.get(client, project)
else:
    work_log = OrderedSetWorkLog(client, project)
work_session = PendulumWorkSession()
logging.info(f"started session for client {client } and project {project}")
input("press enter to end the session...")
logging.info("ending session and pushing to work log...")
work_session.end_session()
work_log.add_session(work_session)
repo.push(work_log)

# A clean code should look like

# logging.basicConfig(level=logging.INFO)
# path, client, project = (sys.argv[1], sys.argv[2], sys.argv[3])
# work_session  = services.start_session(client, project)
# input ("waiting for you to tell me to end stuff...")
# services.end_session(client, project, work_session)

# In this code you did not expose any particular implementation :)
# You could be using any implementation of the service layer functions as well !