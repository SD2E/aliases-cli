"""Tests for our main skele CLI module."""


from unittest import TestCase
from StringIO import StringIO

import sys
from syd.cli import main
from syd import __version__ as VERSION

try:
	from unittest.mock import patch
except:
	from mock import patch

class TestHelp(TestCase):
    def test_returns_usage_information(self):
	testArgs = ['None','-h']
	with patch('sys.argv', testArgs):
		with patch('sys.stdout', StringIO()):
			with self.assertRaises(SystemExit):
				main()
        		self.assertTrue('Usage:' in sys.stdout.getvalue())
	testArgs = ['None','--help']
	with patch('sys.argv', testArgs):
		with patch('sys.stdout', StringIO()):
			with self.assertRaises(SystemExit):
				main()
			self.assertTrue('Usage:' in sys.stdout.getvalue())

class TestVersion(TestCase):
    def test_returns_version_information(self):
	testArgs = ['None','--version']
	with patch('sys.argv', testArgs):
		with patch('sys.stdout', StringIO()):
			with self.assertRaises(SystemExit):
				main()
				self.assertEqual(VERSION in sys.stdout.getvalue())
