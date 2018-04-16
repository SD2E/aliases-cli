#####################
Syd, an Alias Manager
#####################

.. image:: https://travis-ci.org/SD2E/aliases-cli.svg?branch=master
    :target: https://travis-ci.org/SD2E/aliases-cli

.. image:: https://img.shields.io/pypi/l/Django.svg
    :target: https://raw.githubusercontent.com/SD2E/aliases-cli/master/LICENSE

A CLI to manage Reactor and App alias mappings and permissions.

**Features:**

- Retrieve the current Reactor or App identifier for an alias
- Add/update alias mappings to Reactor or App identifiers
- Manage read/write access controls to aliases
- List all aliases, even those shared with you
- Retrieve the current Reactor or App identifier for an alias

Install
=======

If you have not already, install and configure the SD2E _CLI. You should be
able to run the CLI command ``metadata-list`` without error.

Install from GitHub checkout::

    git clone https://github.com/SD2E/aliases-cli
    cd aliases-cli
    python setup.py install


Usage
=====

The name of the CLI tool is ``syd`` and its usage is relatively simple. An
alias can have one and only one value at any given time. Aliases can be shared
with other users via setting their access control list (ACL). The common use
case is to make them visible to any authenticated user by granting the special
user ``world`` read-only access. This is how the SD2 administration team
creates aliases for use by the project at large.

Command and options::

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

Developing
==========

Install in development mode::

    pip install -e .[test]

Run tests::

    # Basic - run tests against your current Python environment
    python setup.py test

    # Advanced - test in other Python environments with tox
    tox

Contributing
------------

Check out the ``develop`` branch and work from it. Create a ``fix`` or
``feat`` branch and commit your changes (including at least minimal test
coverage) and push that branch to GitHub. Check the TravisCI results and
issue a PR against once the tests pass. Changes will be merged into ``master``
by the project maintainer(s).

.. _CLI: https://sd2e.github.io/api-user-guide/docs/install_cli.html
