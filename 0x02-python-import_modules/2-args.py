#!/usr/bin/python3
import sys

length = len(sys.argv)
if length == 1:
        print("0 arguments.")
elif length > 1:
        print("{} arguments:".format(length - 1))
        for i in range(1, length):
                print("{}: {}".format(i, sys.argv[i]))
