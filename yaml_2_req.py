# https://pip.pypa.io/en/stable/reference/pip_install/
# https://pyyaml.org/wiki/PyYAMLDocumentation
import argparse
import os
import re
import sys

import yaml


def main(argv=sys.argv):
    pass


def get_argparse():
    p = argparse.ArgumentParser()

    p.add_argument('--yaml', type=str, default='tests', help='folder')

    p.add_argument('--req', type=str, default='req', help='folder')

    return p


def yaml_to_req(yaml_txt):
    p = yaml.load(yaml_txt)

    req_txt = ''

    if 'name' in p:
        req_txt += f"# name : {p['name']}\n"

    if 'channels' in p:
        req_txt += "# channels :\n"
        for ch in p['channels']:
            req_txt += f"# {ch}\n"

    for lib in p['dependencies']:
        lib_replaced = re.sub(r'\w(\=)\d', ' == ', lib)
        req_txt += f"{lib_replaced}\n"

    return req_txt


if "__main__" == __name__:
    main(sys.argv)
