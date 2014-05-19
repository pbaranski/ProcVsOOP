from unittest import TestCase
import sys
from StringIO import StringIO
from procedural import disc_data_script

__author__ = 'szemek'


class TestDiskScript(TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_disk_script_verbose(self):
        disc_data_script.disk_script(True)
        result = sys.stdout.getvalue().strip()
        self.assertRegexpMatches(result, '(name)(.*)')

    def test_disk_script_info(self):
        disc_data_script.disk_script(False)
        result = sys.stdout.getvalue().strip()
        self.assertRegexpMatches(result, '(name)(.*)')