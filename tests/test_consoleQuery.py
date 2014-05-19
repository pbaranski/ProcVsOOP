from unittest import TestCase
from oop.console_query import ConsoleQuery

__author__ = 'szemek'


class TestConsoleQuery(TestCase):
    def test_out(self):
        out = ConsoleQuery(True)
        expected = out.out()
        self.assertGreater(len(expected.stdout.readlines()), 0, "Impossible! You have no disks:)")