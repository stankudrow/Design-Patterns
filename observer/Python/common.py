#!/usr/bin/env python3
"""Observer Pattern exceptions."""


SettingsType = dict[str, str]


class ObserverPatternError(Exception):
    """Generic Observer Pattern Exception Class."""
