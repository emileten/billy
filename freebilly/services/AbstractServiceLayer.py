import abc
from typing import Tuple
from freebilly.repository.AbstractUnitOfWork import AbstractUnitOfWork
from freebilly.domain.AbstractWorkLog import AbstractWorkLog
from freebilly.domain.AbstractWorkSession import AbstractWorkSession


class AbstractServiceLayer(abc.ABC):

    """
    abstraction over use cases of our app.
    """

    @staticmethod
    @abc.abstractmethod
    def start_session(
        uow: AbstractUnitOfWork, client: str, project: str
    ) -> Tuple[AbstractWorkLog, AbstractWorkSession]:

        """
        Starts a work session and returns it along with the work log specified,
        from existing data if there is or with a brand new one. associated with the client
        and project specified. The session is not yet added to the log because it's still ongoing, not ended.

        Parameters
        ----------
        uow: AbstractUnitOfWork
        client: str
        project: str

        Returns
        -------
        Tuple[AbstractWorkLog, AbstractWorkSession]
            Objects to handle the new session.
        """
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def end_session(
        uow: AbstractUnitOfWork,
        work_log: AbstractWorkLog,
        work_session: AbstractWorkSession,
    ) -> None:

        """
        Ends a work session, and commits it to some repository through a unit of work.

        Parameters
        ----------
        uow: AbstractUnitOfWork
        work_log: AbstractWorkLog
        work_session: AbstractWorkSession
        """
        raise NotImplementedError
