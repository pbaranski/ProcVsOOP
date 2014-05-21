__author__ = 'szemek'


class Disk(object):
    def __init__(self, name='', size=0, free_space=0):
        self.name = name
        self.size = size
        self.free_space = free_space

    def show(self):
        return 'name:', self.name, ' size:', self.size, ' free:', self.free_space
