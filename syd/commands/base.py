"""The base command."""
from agavepy.agave import Agave
from .reactors import alias

class Base(object):
    """A base command."""

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs
        self.store = alias.AliasStore(Agave.restore())

    def run(self):
        raise NotImplementedError('You must implement the run() method yourself!')
