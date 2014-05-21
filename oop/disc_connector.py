from oop.disk import Disk

__author__ = 'szemek'


class DiskConnector(object):
    def __init__(self, console_query):
        self._disks = []
        output = console_query.out()
        for line in output.stdout:
            if line.startswith('Filesystem'):
                continue
            name, size, used, free, used_percent, location = line.split()
            self._disks.append(Disk(name=name, size=size, free_space=free))

    def disks_count(self):
        return len(self._disks)

    def disk_details(self, disk_number):
        disk = self._disks[disk_number]
        return disk.show()

    def disks_names(self):
        #return disk.name list :)
        return [disk.name for disk in self._disks]
