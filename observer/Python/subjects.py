#!/usr/bin/env python3
"""
Observer is a behavioural pattern.

Observers are subscribers, a Subject is a publisher.
A subject can register observers.
All enlisted observers are updated uniformly.
"""

from abc import ABC

from common import (
    ObserverPatternError,
    SettingsType,
)


class Subject(ABC):
    """A generic subject/publisher."""

    def __init__(self):
        self._observers = set()

    def register(self, observer):
        """Adds an observer."""

        if not (hasattr(observer, "update") and callable(observer.update)):
            raise ObserverPatternError(f"{observer} has no `update` method.")
        self._observers.add(observer)

    def unregister(self, observer):
        """Removes an observer."""

        self._observers.remove(observer)

    def notify(self):
        """Performs a uniformed action on all observers."""

        for observer in self._observers:
            observer.update(self)


class FontStylist(Subject):
    """A concrete subject/publisher class."""

    def __init__(self):
        super().__init__()
        self._style: SettingsType = {
            "colour": "black",
            "size": "14pt",
            "font": "Times New Roman",
        }
        print(f"FontStylist: {self._style}")

    @property
    def style(self) -> SettingsType:
        return self._style

    @style.setter
    def style(self, settings: SettingsType):
        self._style = settings
        self.notify()
