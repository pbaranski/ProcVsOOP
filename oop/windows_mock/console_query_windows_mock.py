from subprocess import Popen, PIPE

__author__ = 'A'


class ConsoleQueryWindowsMock(object):
    def __init__(self, detailed):
        self._mocked_output_verbose = 'echo /dev/cciss/c0d0p2      75G   23G   49G  32% /.$echo' \
                                      '/dev/cciss/c0d0p5      24G   22G  1.2G  95% /home.&echo' \
                                      '/dev/cciss/c0d0p3      29G   25G  2.6G  91% /data.&echo' \
                                      '/dev/cciss/c0d0p1     289M   22M  253M   8% /boot.&echo' \
                                      'tmpfs                 252M     0  252M   0% /dev/shm'
        self._mocked_output_info = 'echo /dev/cciss/c0d0p2      75G   23G   49G  32% /.&echo' \
                                   '/dev/cciss/c0d0p5      24G   22G  1.2G  95% /home.&echo' \
                                   'tmpfs                 252M     0  252M   0% /dev/shm'
        self._console_script = self._mocked_output_verbose if detailed is True else self._mocked_output_info

    def out(self):
        return Popen(self._console_script, shell=True, stdout=PIPE, stderr=PIPE)

