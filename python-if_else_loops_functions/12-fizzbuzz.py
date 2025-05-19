#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        c = ""
        if (i % 3 == 0):
            c += "Fizz"
        if (i % 5 == 0):
            c += "Buzz"
        print("{}".format(c) or "{}".format(i), end="")
        print(" ", end="")
