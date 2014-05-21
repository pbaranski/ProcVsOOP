from argparse import ArgumentParser
from oop.disc_app import DiskApp
from oop.windows_mock.disc_app_windows_mock import DiskAppWindowsMock

__author__ = 'A'

description = """\
Running this app shows system disks statistics
"""

if __name__ == "__main__":
    parser = ArgumentParser(description=description)
    parser.add_argument("-v", "--verbosity",
                        help="increase output verbosity\n0 output:INFO\n1 output:VERBOSE",
                        default='0')
    parser.add_argument("-wm", "--winmock",
                        help="enable windows mock for mocking unix like data about disks",
                        action='store_true')
    args = parser.parse_args()

    if args.winmock:
        d = DiskAppWindowsMock()
    else:
        d = DiskApp()

    if args.verbosity in ['0']:
        d.information_level_info()
    else:
        d.information_level_verbose()

    d.print_data_about_all_disks()