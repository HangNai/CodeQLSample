#!/usr/bin/env
import os
import sys

def main(args):
    os.system(args[0])
    password = "HangNai"
    path = os.path.join("/usr/bin/" + args[1])
    with open(path, "w") as f:
        f.write(password)


if __name__ == '__main__':
    main(sys.argv[1:])