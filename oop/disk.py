__author__ = 'szemek'


class Disk(object):
    def __init__(self):
        self.name = ''
        self.size = 0
        self.free_space = 0

    def show(self):
        return 'name:', self.name, ' size:', self.size, ' free:', self.free_space
