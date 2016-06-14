#!/usr/bin/env python
# coding=utf-8

import argparse
import json

import packager


# Parse arguments given via command-line interface
def parse_cli_args():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'config_path',
        help='the path to the utility configuration for this project')
    parser.add_argument(
        '--export', action='store_true',
        help='exports the installed workflow to the local project directory')
    parser.add_argument(
        '--version',
        help='the new version number to use for the workflow')
    return parser.parse_args()


# Locate and parse the configuration for the utility
def get_utility_config(config_path):
    with open(config_path, 'r') as config_file:
        return json.load(config_file)


def main():

    cli_args = parse_cli_args()
    config = get_utility_config(cli_args.config_path)

    packager.package_workflow(
        config,
        version=cli_args.version,
        export=cli_args.export)


if __name__ == '__main__':
    main()
