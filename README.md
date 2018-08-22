# py
Run python expressions as commands. Inspired by the wonderful [rb](https://github.com/thisredone/rb) project by [thisredone](https://github.com/thisredone/rb).

Here's the code (sans options):

```python
#!/usr/bin/env python3

import argparse, base64, collections, collections.abc, csv, gzip, json, math, os, os.path, platform, random, re, sys, time, urllib, uuid, zlib

def execute(_, expression):
    return eval(expression)

for line in sys.stdin:
    result = execute(line.strip(), sys.argv[1])
    if result is not None:
        print(result)
```

## Installation

You have multiple options:

1. Clone this repo and symlink `py` into your path.
2. Run: `sudo curl https://raw.githubusercontent.com/Detry322/py/master/py -o /usr/local/bin/py && sudo chmod +x /usr/local/bin/py`
3. Copy and paste the code from [here](https://raw.githubusercontent.com/Detry322/py/master/py) into a file named `py` in your path.
