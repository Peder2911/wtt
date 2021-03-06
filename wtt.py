#!/usr/bin/env python

import watchgod
import fire
import yaml
import os
import subprocess
import re

def watchthis(dir=".",config=os.path.expanduser("~/.wtt.yaml")):

    print("Watching {dir}".format(dir=os.path.abspath(dir)))

    with open(config) as f:
        config = yaml.safe_load(f)
        

    formats = [e["filetype"] for e in config]
    print("Watching these formats:\n{formats}".format(formats = "\n".join(formats)))

    for c in watchgod.watch(dir):
        change, filepath = c.pop()
        _, ext = os.path.splitext(filepath)

        for e in config:
            if re.search(ext, e["filetype"]):
                call = e["call"].format(file=filepath)
                #os.system("clear")
                os.system(call)


if __name__ == "__main__":
    fire.Fire(watchthis)

