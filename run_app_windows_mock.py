from argparse import ArgumentParser
from oop.windows_mock.disc_app_windows_mock import DiskAppWindowsMock

__author__ = 'A'

description = """\
Running this app shows system disks statistics
"""

if __name__ == "__main__":
    parser = ArgumentParser(description=description)
    parser.add_argument("-v", "--verbosity", help="increase output verbosity\n0 output:INFO\n1 output:VERBOSE",
                        default='0')
    args = parser.parse_args()

    d = DiskAppWindowsMock()

    if args.verbosity in ['1']:
        d.information_level_verbose()
    else:
        d.information_level_info()

    d.print_data_about_all_disks()