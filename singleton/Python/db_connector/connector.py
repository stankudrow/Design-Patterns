#!/usr/bin/env python3

# 1. cd here
# 2. run `python3 connector.py`

import sqlite3
from sys import path

path.insert(0, "..")

from singleton import Singleton


@Singleton
class SQLDataBase:
    """SQLite database [file] class."""

    def __init__(self, conn: str):
        self.conn = sqlite3.connect(conn)
        self.cur = self.conn.cursor()

    def execute(self, stmt: str):
        return self.cur.execute(stmt)


if __name__ == "__main__":
    dbc1 = SQLDataBase("tutorial.db")
    dbc2 = SQLDataBase("tutorial.db")
    assert id(dbc1) == id(dbc2)
    dbc1.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")
    res = dbc2.execute("SELECT name FROM sqlite_master")
    print(f"DB name -> {res.fetchone()}")
