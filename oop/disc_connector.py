from oop.disk import Disk

__author__ = 'szemek'


class DiskConnector(object):
    def __init__(self, console_query):
        self._disks = []
        output = console_query.out()
        output_lines = output.stdout.readlines()
        for line in output_lines:
            line = line.split()
            disk = Disk()
            disk.name = line[0]
            disk.size = line[1]
            disk.free_space = line[3]
            self._disks.append(disk)

    def disks_count(self):
        return len(self._disks)

    def disk_details(self, disk_number):
        disk = self._disks[disk_number]
        return disk.show()

    def disks_names(self):
        #return disk.name list :)
        return [disk.name for disk in self._disks]
