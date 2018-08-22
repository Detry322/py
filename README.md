# py
Run python expressions as commands. Inspired by the wonderful [rb](https://github.com/thisredone/rb) project by [thisredone](https://github.com/thisredone/rb).

Here's the code (sans options):

```python
#!/usr/bin/env python3

import argparse, base64, collections, collections.abc, csv, glob, gzip, json, math, os, os.path, platform, random, re, sys, time, urllib, uuid, zlib

def execute(_, expression):
    return eval(expression)

for line in sys.stdin:
    result = execute(line.strip(), sys.argv[1])
    if result is not None:
        print(result)
```

Here's some examples:

```sh
# Filter lines outside a range
seq 1 100 | ./py "_ if 50 < int(_) < 60 else None"

# Retreive data from a CSV
cat demodata.csv | py -f "map(lambda l: l['weekdays'], csv.DictReader(_))"
```

`py`'s benefit is that it lets you write scripts in a language you're familiar with (python) and saves you from one you might make mistakes in (bash).


## Installation

You have multiple options:

1. Clone this repo and symlink `py` into your path.
2. Run: `sudo curl https://raw.githubusercontent.com/Detry322/py/master/py -o /usr/local/bin/py && sudo chmod +x /usr/local/bin/py`
3. Copy and paste the code from [here](https://raw.githubusercontent.com/Detry322/py/master/py) into a file named `py` in your path.

## Options

```
usage: py [-h] [-g] [-f] [-s] [-n] expression

Run one-line python expressions on stdin. The expression has access to local
variable _, containing a single line of input. The expression
also has access to common python stdlib modules (sorted alphabetically):
argparse, base64, collections, csv, glob, gzip, json, math, os, os.path,
platform, random, re, sys, time, urllib, uuid, zlib

positional arguments:
  expression       The expression to run.

optional arguments:
  -h, --help       show this help message and exit
  -g, --generator  Pass stdin as a generator. _ returns stripped lines of
                   stdin
  -f, --file       Pass stdin as a file. _ is set to sys.stdin.
  -s, --string     Pass stdin as a string. _ is set to sys.stdin.read().
  -n, --none       Print None results.
```

## Examples

**Retreive data from a CSV**
```sh
cat demodata.csv | py -f "map(lambda l: l['weekdays'], csv.DictReader(_))"
```

**Filter lines outside a range**
```sh
seq 1 100 | ./py "_ if 50 < int(_) < 60 else None"
```

**Compress and output each file in the working directory**
```sh
ls | ./py '"{}: {}".format(_, base64.b64encode(zlib.compress(open(_, "rb").read())).decode("ascii"))'
```
