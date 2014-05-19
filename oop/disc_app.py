from oop.console_query import ConsoleQuery
from oop.disc_connector import DiskConnector

__author__ = 'szemek'


class DiskApp(object):
    def __init__(self):
        query = ConsoleQuery(False)
        self.__disk_connector = DiskConnector(query)

    def disks_count(self):
        return self.__disk_connector.disks_count()

    def disks_names(self):
        print self.__disk_connector.disks_names()

    def print_data_about_all_disks(self):
        for i in range(0, self.__disk_connector.disks_count()):
            print self.__disk_connector.disk_details(i)

    def information_level_verbose(self):
        query = ConsoleQuery(True)
        self.__disk_connector = DiskConnector(query)

    def information_level_info(self):
        query = ConsoleQuery(False)
        self.__disk_connector = DiskConnector(query)


if __name__ == "__main__":
    d = DiskApp()
    d.information_level_verbose()
    d.print_data_about_all_disks()