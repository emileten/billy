import abc
from typing import Tuple
from src.freebilly.repository.AbstractUnitOfWork import AbstractUnitOfWork
from src.freebilly.domain.AbstractWorkLog import AbstractWorkLog
from src.freebilly.domain.AbstractWorkSession import AbstractWorkSession


class AbstractServiceLayer(abc.ABC):

    """
    abstraction over the layer where 'services' are performed : jobs that can be identified to what a user actually
    needs to do with work sessions and work logs.
    """

    @abc.abstractmethod
    def start_session(
        self, uow: AbstractUnitOfWork, client: str, project: str
    ) -> Tuple[AbstractUnitOfWork, AbstractWorkLog, AbstractWorkSession]:

        """
        Starts a work session and provides the objects needed to manage it.

        Parameters
        ----------
        path: Path
        client: str
        project: str

        Returns
        -------
        Tuple[AbstractUnitOfWork, AbstractWorkLog, AbstractWorkSession]
            Objects to handle the new session.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def end_session(
        self,
        uow: AbstractUnitOfWork,
        work_log: AbstractWorkLog,
        work_session: AbstractWorkSession,
    ) -> None:

        """
        Ends a work session, and commits it to some repository through a unit of work.

        Parameters
        ----------
        repo: AbstractUnitOfWork
        work_log: AbstractWorkLog
        work_session: AbstractWorkSession
        """
        raise NotImplementedError
