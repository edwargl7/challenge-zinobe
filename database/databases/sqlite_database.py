"""
SQLite3 database.
Functions to manage the sqlite database.
"""
import sqlite3
from sqlite3 import Error

# Databases
from database.databases.database_interface import DatabaseInterface


class SQLiteDatabase(DatabaseInterface):
    """SQLite Database.
    Manage sqlite databases (connections and queries).
    """

    def __init__(self, db_credentials):
        super().__init__(db_credentials)

    def __connect_database(self):
        connection = None
        msg = ''
        try:
            connection = sqlite3.connect(self._db_credentials['database_name'])
            print('SQLite connection created')
        except (Exception, Error) as error:
            msg = f'Error while connecting to SQLite. {error}'
        finally:
            return connection, msg

    @staticmethod
    def __close_connection(connection, cursor=None):
        if connection:
            if cursor:
                cursor.close()
            connection.close()
            print('SQLite connection is closed')

    def __execute_query(self, connection, query, args=None, commit=False):
        cursor = None
        try:
            if connection:
                cursor = connection.cursor()
                if args:
                    cursor.execute(query, args)
                else:
                    cursor.execute(query)
                if commit:
                    connection.commit()
        except (Exception, Error) as error:
            print(f'Error while querying the database. {error}')
        finally:
            return cursor

    def valid_connection(self) -> bool:
        connection, msg = self.__connect_database()
        if connection:
            connection.close()
            print('SQLite connection is closed')
            return True
        else:
            print(msg)
            return False

    def query_all(self, query, args=None, commit=False) -> list:
        connection, msg = self.__connect_database()
        cursor = None
        result = None
        try:
            cursor = self.__execute_query(connection, query, args, commit)
            if cursor:
                result = [dict(row) for row in cursor.fetchall()]
        except (Exception, Error) as error:
            print(f'Error while querying the database. {error}')
        finally:
            self.__close_connection(connection, cursor)
            return result

    def query_many(self, n, query, args=None, commit=False) -> list:
        connection, msg = self.__connect_database()
        cursor = None
        result = None
        try:
            cursor = self.__execute_query(connection, query, args, commit)
            if cursor:
                result = [dict(row) for row in cursor.fetchmany(n)]
        except (Exception, Error) as error:
            print(f'Error while querying the database. {error}')
        finally:
            self.__close_connection(connection, cursor)
            return result

    def query_one(self, query, args=None, commit=False) -> dict:
        connection, msg = self.__connect_database()
        cursor = None
        result = None
        try:
            cursor = self.__execute_query(connection, query, args, commit)
            if cursor and not commit:
                result = dict(cursor.fetchone())
            if cursor and commit:
                result = cursor.lastrowid
        except (Exception, Error) as error:
            print(f'Error while querying the database. {error}')
        finally:
            self.__close_connection(connection, cursor)
            return result

    def create_table(self, query):
        connection, msg = self.__connect_database()
        cursor = None
        result = None
        try:
            cursor = self.__execute_query(connection, query, None, True)
        except (Exception, Error) as error:
            print(f'Error while querying the database. {error}')
        finally:
            self.__close_connection(connection, cursor)
