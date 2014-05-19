from unittest import TestCase
import sys
from StringIO import StringIO
from oop.disc_app import DiskApp

__author__ = 'szemek'


class TestDiskApp(TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_disks_count(self):
        d = DiskApp()
        self.assertGreater(d.disks_count(), 0, "No disks found.")

    def test_print_data_about_all_disks_verb(self):
        d = DiskApp()
        d.information_level_verbose()
        d.print_data_about_all_disks()
        result = sys.stdout.getvalue().strip()
        self.assertRegexpMatches(result, '(name)(.*)')

    def test_print_data_about_all_disks_info(self):
        d = DiskApp()
        d.information_level_info()
        d.print_data_about_all_disks()
        result = sys.stdout.getvalue().strip()
        self.assertRegexpMatches(result, '(name)(.*)')