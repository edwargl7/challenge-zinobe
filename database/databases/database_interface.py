"""Database Interface
Interface to manage databases (connections and queries)
"""
import abc


class DatabaseInterface(metaclass=abc.ABCMeta):
    """Database Interface.
    Interface to manage databases (connections and queries).
    """

    def __init__(self, db_credentials):
        """Constructor
        :param db_credentials: database credentials.
        :type db_credentials: dict
        """
        self._db_credentials = db_credentials

    @abc.abstractmethod
    def valid_connection(self) -> bool:
        """Validate the connection to the database.
        :return: true if the connection of the database is valid;
            otherwise, it returns false.
        """

    @abc.abstractmethod
    def query_all(self, query, args=None, commit=False) -> list:
        """Query that return all rows.
        :param query: query for the database.
        :type query: str
        :param args: query arguments, optional.
        :param commit: Flag to do commit.
        :return: row list.
        """

    @abc.abstractmethod
    def query_many(self, n, query, args=None, commit=False) -> list:
        """Query with a row limit.
        :param n: row limit.
        :type n: int
        :param query: query for the database.
        :type query: str
        :param args: query arguments
        :param commit: Flag to do commit.
        :return: row list.
        """

    @abc.abstractmethod
    def query_one(self, query, args=None, commit=False) -> dict:
        """Query that return one row or value.
        :param query: query for the database.
        :type query: str
        :param args: query arguments
        :param commit: Flag to do commit.
        :return: row or value
        """