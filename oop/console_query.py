from subprocess import Popen, PIPE

__author__ = 'szemek'


class ConsoleQuery(object):
    def __init__(self, detailed):
        self._console_script = 'df -ha' if detailed is True else 'df -h | grep /dev/sd'

    def out(self):
        return Popen(self._console_script, shell=True, stdout=PIPE, stderr=PIPE)