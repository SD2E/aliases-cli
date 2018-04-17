"""Tests for our main skele CLI module."""


from unittest import TestCase

import sys
from syd.cli import main
from syd import __version__ as VERSION

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

class TestHelp(TestCase):
    def test_returns_usage_information(self):
        testArgs = ['None', '-h']
        with patch('sys.argv', testArgs):
            with patch('sys.stdout', StringIO()):
                with self.assertRaises(SystemExit):
                    main()
                self.assertTrue('Usage:' in sys.stdout.getvalue())
        testArgs = ['None', '--help']
        with patch('sys.argv', testArgs):
            with patch('sys.stdout', StringIO()):
                with self.assertRaises(SystemExit):
                    main()
                self.assertTrue('Usage:' in sys.stdout.getvalue())

class TestVersion(TestCase):
    def test_returns_version_information(self):
        testArgs = ['None', '--version']
        with patch('sys.argv', testArgs):
            with patch('sys.stdout', StringIO()):
                with self.assertRaises(SystemExit):
                    main()
                self.assertEqual(VERSION, sys.stdout.getvalue().rstrip())
