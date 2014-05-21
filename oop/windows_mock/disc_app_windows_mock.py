from oop.disc_connector import DiskConnector
from oop.windows_mock.console_query_windows_mock import ConsoleQueryWindowsMock

__author__ = 'szemek'


class DiskAppWindowsMock(object):
    def __init__(self):
        query = ConsoleQueryWindowsMock(False)
        self.__disk_connector = DiskConnector(query)

    def disks_count(self):
        return self.__disk_connector.disks_count()

    def disks_names(self):
        print self.__disk_connector.disks_names()

    def print_data_about_all_disks(self):
        for i in range(0, self.__disk_connector.disks_count()):
            print self.__disk_connector.disk_details(i)

    def information_level_verbose(self):
        query = ConsoleQueryWindowsMock(True)
        self.__disk_connector = DiskConnector(query)

    def information_level_info(self):
        query = ConsoleQueryWindowsMock(False)
        self.__disk_connector = DiskConnector(query)