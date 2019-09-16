import argparse
import os
import sys


def main(argv=sys.argv):
    pass


def get_argparse():

    p = argparse.ArgumentParser()

    p.add_argument('--yaml', type=str, default='tests', help='folder')

    p.add_argument('--req', type=str, default='req', help='folder')

    return p


if "__main__" == __name__:
    main(sys.argv)
