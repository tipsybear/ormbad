# ormbad.engine
# Connection and configuration parameters for the databases
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Fri Jun 12 14:11:56 2015 -0400
#
# Copyright (C) 2015 Tipsy Bear Studios
# For license information, see LICENSE.txt
#
# ID: engine.py [] benjamin@bengfort.com $

"""
Connection and configuration parameters for the databases

Really helpful SlideShare:
http://www.slideshare.net/petereisentraut/programming-with-python-and-postgresql
"""

##########################################################################
## Imports
##########################################################################

import psycopg2
import psycopg2.extras

from DBUtils.PersistentDB import PersistentDB

from ormbad.config import settings
from ormbad.exceptions import DatabaseConnectionError

##########################################################################
## Database Engine
##########################################################################

class DatabaseEngine(object):
    """
    Thin wrapper around a peristent database connection pool.
    """

    def __init__(self, **kwargs):
        """
        Provide database connection parameters as keyword arguments.
        """
        param = lambda name: kwargs.get(name, settings.database[name])

        # Internal connection pool
        self._persist    = PersistentDB(psycopg2, **{
            "database": param('name'),
            "user": param('user'),
            "password": param('password'),
            "host": param('host'),
            "port": param('port'),
            "failures": DatabaseConnectionError,
            "cursor_factory": psycopg2.extras.NamedTupleCursor,
        })

    def connection(self):
        """
        Return a reference to the persistent connection
        """
        return self._persist.connection()

##########################################################################
## Module level singleton - always use the session object!
##########################################################################

session = DatabaseEngine()

if __name__ == '__main__':
    db = session.connection()
    cursor = db.cursor()
    cursor.execute("SELECT count(id) as clients FROM client")
    print "{row.clients} clients in the database".format(row=cursor.fetchone())

    db = session.connection()
    cursor = db.cursor()
    cursor.execute("SELECT count(id) as organizations FROM organization")
    print "{row.organizations} clients in the database".format(row=cursor.fetchone())
