# https://pip.pypa.io/en/stable/reference/pip_install/
# https://pyyaml.org/wiki/PyYAMLDocumentation
import argparse
import os
import re
import sys

import yaml


def main(argv=sys.argv):
    p = get_argparse()

    ns = p.parse_args(argv[1:])

    os.makedirs(ns.req, exist_ok=True)

    for yaml_filename in os.listdir(ns.yaml):
        with open(os.path.join(ns.yaml, yaml_filename), 'rt') as yaml_fp:
            yaml_txt = yaml_fp.read()

        req_txt = yaml_to_req(yaml_txt)

        if not ns.dry_run:
            with open(os.path.join(ns.req, yaml_filename), 'wt') as req_fp:
                req_fp.write(req_txt)
        else:
            print('## write to', os.path.join(ns.req, yaml_filename))
            print(req_txt)


def get_argparse():
    p = argparse.ArgumentParser()

    p.add_argument('--yaml', type=str, default='tests', help='folder')
    p.add_argument('--req', type=str, default='req', help='folder')
    p.add_argument('--dry-run', default=False, action='store_true')

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
