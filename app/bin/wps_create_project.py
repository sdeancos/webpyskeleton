#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import stderr, argv
from argparse import ArgumentParser
from os.path import dirname, abspath, join, pardir
from distutils.dir_util import copy_tree

PATH = abspath(dirname(argv[0]))
PATH_APP = abspath(join(join(PATH, pardir), pardir))


def generate(path=None):
    if path:
        stderr.write('Generate Skeleton Bundle: ' + str(path) + '\n')
        copy_tree(PATH_APP, path)

        stderr.write('Generate Project: ' + str(path) + '\n')
        return 0
    else:
        return 1

if __name__ == '__main__':
    arg_parser = ArgumentParser(description='Create Project')
    arg_parser.add_argument('-p', '--path', type=str, help='Project name')
    args = arg_parser.parse_args()
    if args.path:
        generate(args.path)
    else:
        stderr.write('Project name not valid: ' + str(args.path) + '\n')
        stderr.write('-p --path ProjectName\n')
