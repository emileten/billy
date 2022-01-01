from src.freebilly.endpoint.AbstractEndPoint import AbstractEndPoint
import click


class ClickEndPoint(AbstractEndPoint):
    def record_session(self, path: str, client: str, project: str) -> None:

        raise NotImplementedError


from src.freebilly.services.ConcreteServiceLayer import ConcreteServiceLayer

# import sys
# import logging
# import pathlib
#
#
# logging.basicConfig(level=logging.INFO)
# path, client, project = (sys.argv[1], sys.argv[2], sys.argv[3])
# logging.info(f"started session for client {client } and project {project}")
# repo, work_log, work_session = services_start_session(path, client, project)
# input("press enter to end the session...")
# logging.info("ending session and pushing to work log...")
# services_end_session(work_session, work_log)
#
#
#
#
#
#
#
#
# repo = CsvRepository(pathlib.Path(path))
# if repo.exists(client, project):
#     work_log = repo.get(client, project)
# else:
#     work_log = OrderedSetWorkLog(client, project)
# work_session = PendulumWorkSession()
# logging.info(f"started session for client {client } and project {project}")
# input("press enter to end the session...")
# logging.info("ending session and pushing to work log...")
#
# services_end_session(work_session, work_log)
# A clean code should look like

# logging.basicConfig(level=logging.INFO)
# path, client, project = (sys.argv[1], sys.argv[2], sys.argv[3])
# work_session  = services.start_session(client, project)
# input ("waiting for you to tell me to end stuff...")
# services.end_session(client, project, work_session)

# In this code you did not expose any particular implementation :)
# You could be using any implementation of the service layer functions as well !
