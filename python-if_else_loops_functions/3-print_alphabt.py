#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    c = chr(i)
    if c != "e" and c != "q":
        print("{}".format(chr(i)), end='')
