#!/usr/bin/env python3
"""
Observer is a behavioural pattern.

Observers/Subscribers are objects
that are notified by a Subject/Publisher.

An object "willing" to be updated from a subject,
enlists into the ranks of subscribers.

A subject will notify all its observers.
Un- or subscribing is done at runtime.
"""


from abc import ABC, abstractmethod


class Observer(ABC):
    """A generic observer."""

    @abstractmethod
    def update(self, subject):
        raise NotImplementedError


class Paragraph(Observer):
    """A paragraph as a concrete observer."""

    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.style = {}  # just for simplicity

    def __repr__(self) -> str:
        return f"Paragraph {self.name}: {self.style}"

    def update(self, font_subject):
        self.style = font_subject.style
        print(f"Paragraph {self.name} has been notified")