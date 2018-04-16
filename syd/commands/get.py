"""The hello command."""

from .base import Base


class GetId(Base):
    """Retrieve the ID mapped to a given alias"""

    def run(self):
        api_id = self.store.get_name(self.options['<alias>'])
        print(api_id)
