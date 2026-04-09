import argparse
import os
import sys

from . import data

def main():
    args = parse_args()
    args.func(args)


def parse_args():
	#Creates new argument parser
    parser = argparse.ArgumentParser()

    #Must provide subcommands like 'init'
    commands = parser.add_subparsers(dest='command')
    commands.required = True

    #Practice: Checking for understanding
    clone_parser = commands.add_parser('clone')
    clone_parser.set_defaults(func=clone)

    #Creates sub command called 'init'
    init_parser = commands.add_parser('init')
    #Links 'init' command to def init(args)
    init_parser.set_defaults(func=init)

    #Makes the object/file into hash1
    hash_object_parser = commands.add_parser('hash-object')
    hash_object_parser.set_defaults(func=hash_object)
    hash_object_parser.add_argument('file')

    #Returns the object's/file's contents
    cat_file_parser = commands.add_parser('cat-file')
    cat_file_parser.set_defaults(func=cat_file)
    cat_file_parser.add_argument('object')

    return parser.parse_args()

def init(args):
    data.init()
    print(f'Initialized empty ugit repository in {os.getcwd()}/{data.GIT_DIR}')

def clone(args):
	print('Hello from clone')

def hash_object(args):
    with open(args.file, 'rb') as f:
        print(data.hash_object(f.read()))

def cat_file(args):
    #Immediately writes out everything in the buffer 
    sys.stdout.flush()
    sys.stdout.buffer.write(data.get_object(args.object))


