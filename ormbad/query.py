# ormbad.query
# Database query helper module for executing pooled, large queries
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Wed Jun 17 16:54:57 2015 -0400
#
# Copyright (C) 2015 Tipsy Bear Studios
# For license information, see LICENSE.txt
#
# ID: query.py [] benjamin@bengfort.com $

"""
Database query helper module for executing pooled, large queries
"""

##########################################################################
## Imports
##########################################################################

import time

from ormbad.engine import session
from ormbad.exceptions import BadDatabaseQuery

##########################################################################
## Helper Function
##########################################################################

def get_cursor_name(prefix="ormbad"):
    """
    Returns a unique cursor name by appending the timestamp to the prefix
    """
    ts = int(round(time.time() * 1000))
    return "{:s}_{:d}".format(prefix, ts)

##########################################################################
## Simple Query
##########################################################################

class Query(object):
    """
    Wraps a SQL string to execute against the database. Pass in a
    parameterized SQL string (e.g. with format characters) then execute the
    statement against the database using arbitrary queries.
    """

    def __init__(self, sql, large=False, single=False):
        """
        If query is large, then uses a serverside cusor to fetch in batches.
        If query is single, then returns a result rather than a generator.
        """
        self.stmt    = sql
        self.large   = large
        self.single  = single

    def cursor(self):
        """
        Returns a cursor for the query
        """
        dbconn  = session.connection()
        if self.large:
            return dbconn.cursor(name=get_cursor_name())
        return dbconn.cursor()

    def query(self, *args, **kwargs):
        """
        Executes the query with the given arguments OR keyword arguments.
        Pass in either args or kwargs; raises a BadDatabaseQuery if both.

        Currently this simply returns cursor, but in the future the query
        will have a context manager associated with it.
        """
        if args and kwargs:
            raise BadDatabaseQuery(
                "Cannot pass in both position and keyword arguments "
                "to execute a sql query. Make sure query is correctly formed."
            )

        params = args or kwargs
        cursor = self.cursor()
        cursor.execute(self.stmt, params)
        return self.QueryResult(cursor, self.single)

    def count(self, *args, **kwargs):
        """
        Helper method that wraps a count(*) around the query passed in and
        executes the count against the database with the parameters provided.
        """
        count = Query("SELECT count(*) FROM ({}) AS {}".format(self.stmt, get_cursor_name()))
        with count.query(*args, **kwargs) as result:
            return result.get()

    class QueryResult(object):
        """
        A context manager for wrapping an executed cursor so that the cursor
        is automatically closed. Also provides iterable functions and other
        quality checks on the database query.
        """

        def __init__(self, cursor, single=False):
            self.cursor = cursor
            self.single = single

        def __enter__(self):
            return self

        def __exit__(self, type, value, tb):
            self.cursor.close()

        def __iter__(self):
            for row in self.cursor:
                yield row

        def commit(self):
            self.cursor.connection.commit()

        def get(self):
            return self.cursor.fetchone()
