class Singleton:
	"""Singleton structural design pattern."""

	def __init__(self, klass):
		self._klass = klass
		self._instance = None

	def __call__(self, *args, **kwargs):
		if self._instance is None:
			self._instance = self._klass(*args, **kwargs)
		return self._instance
