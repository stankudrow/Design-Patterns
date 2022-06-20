# Inspired by "Practical Python Design Patterns", Wessel Badenhorst
# https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
# https://github.com/Kemaweyan/singleton_decorator


class Singleton:
    """Singleton structural design pattern."""

    def __init__(self, klass):
        self._klass = klass
        self._instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self._klass(*args, **kwargs)
        return self._instance
