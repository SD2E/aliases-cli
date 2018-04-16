#!/usr/bin/env python

from .base import Base


class RemAlias(Base):
    """Delete an alias"""

    def run(self):
        response = self.store.rem_alias(
            alias=self.options['<alias>'])
        if response is False:
            print("Could not delete {}".format(self.options['<alias>']))
