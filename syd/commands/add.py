"""The add command."""
from .base import Base


class SetAlias(Base):
    """Add or update an Alias"""

    def run(self):
        response = self.store.set_alias(
            alias=self.options['<alias>'], name=self.options['<id>'])
        print("{}".format(response))
