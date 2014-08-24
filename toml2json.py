#!/usr/bin/env python

from __future__ import print_function

import datetime
import json
import sys

import toml


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            # http://stackoverflow.com/q/19654578/1558890
            return obj.isoformat() + "Z"
        return super(CustomEncoder, self).default(obj)


def toml2json(s):
    return json.dumps(toml.loads(s), cls=CustomEncoder)


def json2toml(s):
    return toml.dumps(json.loads(s))


def main(cmd=None):
    if cmd is None:
        cmd = sys.argv[0]

    if "toml2json" in cmd:
        func = toml2json
    elif "json2toml" in cmd:
        func = json2toml
    else:
        raise RuntimeError("Must be called either as `toml2json` or `json2toml`.")

    if not len(sys.argv) == 2:
        # FIXME
        raise RuntimeError("Must be called with a filename as argument.")

    with open(sys.argv[1]) as f:
        s = f.read()
    result = func(s)
    print(result)


if __name__ == "__main__":
    main()
