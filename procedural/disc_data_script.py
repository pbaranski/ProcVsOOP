__author__ = 'szemek'
from subprocess import Popen, PIPE


def console_query():
    return Popen('df -h | grep /dev/sd', shell=True, stdout=PIPE, stderr=PIPE)


def console_query_details():
    return Popen('df -h', shell=True, stdout=PIPE, stderr=PIPE)


def disk_script(print_details):
    output = console_query_details() if print_details is True else console_query()
    output_lines = output.stdout.readlines()
    for line in output_lines:
        line = line.split()
        print 'name:', line[0], ' size:', line[1], ' free:', line[3]

if __name__ == "__main__":
    disk_script(True)