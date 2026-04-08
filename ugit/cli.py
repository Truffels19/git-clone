import argparse
import os

from . import data

def main():
    args = parse_args()
    args.func(args)


def parse_args()):
	#Creates new argument parser
    parser = argparse.ArgumentParser()

    #Must provide subcommans like 'init'
    commands = parser.add_subparsers(dest='command')
    commands.required = True

    #Checking for understanding
    clone_parser = commands.add_parser('clone')
    clone_parser.set_defaults(func=clone)

    #Creates sub command called 'init'
    init_parser = commands.add_parser('init')
    #Links 'init' command to def init(args)
    init_parser.set_defaults(func=init)

    return parser.parse_args()


def init (args):
    data.init()
    print(f'Initialized empty ugit repository in {os.getcwd()}/{data.GIT_DIR}')

def clone (args):
	print('Hello from clone')
