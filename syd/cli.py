"""
syd - A manager for App and Reactor aliases

Usage:
  syd ls [--sorted]
  syd get <alias>
  syd add <alias> <id>
  syd rem <alias>
  syd acl <alias> ([<user>] [--read|--noread] [--write|--nowrite])
  syd -h | --help
  syd --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.
  --sorted                          Sort list results alphabetically

Examples:
  $ syd add youve-got-mail EWPrqWNDqZ7p8
  $ syd get youve-got-mail
  EWPrqWNDqZ7p8
  $ syd add youve-got-mail PrqWW8qZ7NDEp
  $ syd get youve-got-mail
  PrqWW8qZ7NDEp
  $ syd acl youve-got-mail
  vaughn - Read: True Write: True
  $ syd acl youve-got-mail taco --read --write
  taco - Read: True Write: False
  $ syd acl youve-got-mail taco --noread
  $ syd rem youve-got-mail

Having trouble?:
  Get help from a person:
  - support@sd2e.org
  Report issues or contribute fixes
  - https://github.com/SD2E/aliases-cli
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import syd.commands

    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
        if hasattr(syd.commands, k) and v:
            module = getattr(syd.commands, k)
            syd.commands = getmembers(module, isclass)
            command = [command[1] for command in syd.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
