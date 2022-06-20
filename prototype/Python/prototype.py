# Inspired by "Practical Python Design Patterns", Wessel Badenhorst
# https://radek.io/2011/08/03/design-pattern-prototype/


from abc import ABC, abstractmethod
from copy import deepcopy


class Cloner(ABC):
    """Prototype creational design pattern."""

    @abstractmethod
    def clone(self):
        raise NotImplementedError


class VirusCloner(Cloner):
    """A concrete cloner associated with a (Virus) client."""

    def clone(self):
        return deepcopy(self)
