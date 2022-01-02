import abc

# we could have a set of functions already implemented. We use the idea of an interface just to state clearly what we expect the
# code to look like.


class AbstractEndPoint(abc.ABC):

    """
    abstraction over an interface for this app use cases. Implementations of this abstract class are the closest
    point of the app to the user's actions.
    """

    @staticmethod
    @abc.abstractmethod
    def record_session(path: str, client: str, project: str) -> None:

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
