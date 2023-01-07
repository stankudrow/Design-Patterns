#!/usr/bin/env python3
"""See observers.py for explanations."""


class Subject:
    """A generic subject/publisher."""

    def __init__(self):
        print("Subject: no observers yet.")
        self._observers = []

    def register(self, observer):
        """Registers an observer willing notifications."""
        if observer not in self._observers:
            # let's not check if an observer really has `update` method.
            self._observers.append(observer)

    def unregister(self, observer):
        """Unsubscribes an observer from the service list."""
        # yes, errors/exceptions are not bad.
        self._observers.remove(observer)

    def notify(self):
        """Performs a uniformed action on all observers."""
        for observer in self._observers:
            # Yes, observers have interface
            # for being capable for receiving notifications.
            observer.update(self)


class FontStylist(Subject):
    """A concrete subject/publisher class."""

    def __init__(self):
        super().__init__()
        print("A ConcreteSubject: FontStylist.")
        self._style = {
            "colour": "black",
            "size": "14pt",
            "font": "Times New Roman",
        }

    @property
    def style(self) -> dict[str, str]:
        return self._style

    @style.setter
    def style(self, settings: dict[str, str]):
        self._style = settings
        self.notify()  # !!!
