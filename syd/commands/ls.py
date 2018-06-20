"""The ls command."""
from .base import Base


class GetAliases(Base):
    """Retrieve list of known aliases"""

    def run(self):
        print('Aliases:')
        sortlist = self.options.get('--sorted', False)
        aliases = self.store.get_aliases(sort_aliases=sortlist)
        for alias in aliases:
            print("  {}".format(str(alias)))
