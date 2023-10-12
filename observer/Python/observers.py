#!/usr/bin/env python3
"""
Observer is a behavioural pattern.

Observers are subscribers, a Subject is a publisher.
A subject can register observers.
All enlisted observers are updated uniformly.
"""


from abc import ABC, abstractmethod

from common import SettingsType


class Observer(ABC):
    """A generic observer."""

    @abstractmethod
    def update(self, subject):
        raise NotImplementedError


class Paragraph(Observer):
    """A paragraph as a concrete observer."""

    def __init__(self, name: str):
        self.name = name
        self.style: SettingsType = {}

    def __repr__(self) -> str:
        return f"Paragraph -> {self.name}: {self.style}"

    def update(self, font_subject):
        self.style = font_subject.style
        print(f"Paragraph -> {self.name} has been notified")
