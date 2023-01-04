#!/usr/bin/env python3

# 1. cd here
# 2. run `python3 logger.py`

from os import PathLike
from sys import path
from typing import Union

path.insert(0, "..")

from singleton import Singleton


@Singleton
class Logger:
    """Logger class."""

    def __init__(self, out: Union[str, bytes, PathLike]):
        self.out = out

    def log(self, level: str, msg: str):
        with open(self.out, "a") as outfile:
            outfile.write(f"[{level}]: {msg}\n")

    def debug(self, msg: str):
        self.log("debug", msg)

    def error(self, msg: str):
        self.log("error", msg)

    def info(self, msg: str):
        self.log("info", msg)

    def warn(self, msg: str):
        self.log("warn", msg)


# breakpoint()

if __name__ == "__main__":
    lgr1 = Logger("logger1.txt")
    lgr2 = Logger("logger2.txt")
    assert id(lgr1) == id(lgr2)
    lgr1.info(f"Logger1: id = {id(lgr1)}")
    lgr2.debug(f"Logger2 id = {id(lgr2)}")
    lgr2.warn(f"assert: {id(lgr1) == id(lgr2)}")
