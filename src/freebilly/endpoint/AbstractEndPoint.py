import abc

class AbstractEndPoint(abc.ABC):

    """
    abstraction over an interface to record work sessions
    """

    def record_session(self, path: str, client: str, project: str) -> None :

        """
        starts a work session, waits for the user to give the signal to end it and binds it
        to a work log identified by a path, a client and a project.

        Parameters
        ----------
        path : str
        client: str
        project: str
        """

        raise NotImplementedError
