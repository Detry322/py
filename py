#!/usr/bin/env python3
"""\
Run one-line python expressions on stdin.

The expression has access to local variable _, containing a single line of input.
The expression also has access to common python stdlib modules (sorted alphabetically):

argparse, base64, collections, csv, glob, gzip, json, math, os, os.path, platform, random, re, sys, time, urllib, uuid, zlib
"""

import argparse, base64, collections, collections.abc, csv, glob, gzip, json, math, os, os.path, platform, random, re, sys, time, urllib, uuid, zlib

def execute(_, expression):
    return eval(expression)

def print_(result, print_none=False):
    if isinstance(result, collections.abc.Iterable) and not isinstance(result, str):
        for element in result:
            print_(element, args)
    else:
        if result is not None or print_none:
            print(result)

def strip_newlines(stdin):
    for line in stdin:
        yield line.strip()

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('expression', type=str, help='The expression to run.')
parser.add_argument('-g', '--generator', action='store_true', help="Pass stdin as a generator. _ returns stripped lines of stdin")
parser.add_argument('-f', '--file', action='store_true', help="Pass stdin as a file. _ is set to sys.stdin.")
parser.add_argument('-s', '--string', action='store_true', help="Pass stdin as a string. _ is set to sys.stdin.read().")
parser.add_argument('-n', '--none', action='store_true', help="Print None results.")
args = parser.parse_args()

if args.generator:
    print_(execute(strip_newlines(sys.stdin), args.expression), print_none=args.none)
elif args.file:
    print_(execute(sys.stdin, args.expression), print_none=args.none)
elif args.string:
    print_(execute(sys.stdin.read(), args.expression), print_none=args.none)
else:
    for line in sys.stdin:
        print_(execute(line.strip(), args.expression), print_none=args.none)
