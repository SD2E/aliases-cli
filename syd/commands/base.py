"""The base object"""
from agavepy.agave import Agave
from .reactors import aliases


class Base(object):
    """Base object for implementing commands."""

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs
        self.store = aliases.store.AliasStore(
            Agave.restore(),
            aliasPrefix='v1-alias-')

    def run(self):
        raise NotImplementedError(
            'You must implement the run() method yourself!')
