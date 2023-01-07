#!/usr/bin/env python3
"""
The Borg pattern is also known as the Monostate pattern.

# Inspired by "Mastering Python", Rick van Hattem, Packt.
# https://code.activestate.com/recipes/66531/
# https://github.com/faif/python-patterns/blob/master/patterns/creational/borg.py
# https://milovantomasevic.com/courses/python-design-patterns-borg/
# https://medium.com/@snk.nitin/design-patterns-and-where-to-find-them-ab57aef6f62a
# https://peps.python.org/pep-0412/
"""


class Borg:
    """Borg is behavioural pattern: one state across all instances."""

    _state = {}

    def __init__(self):
        self.__dict__ = self._state
