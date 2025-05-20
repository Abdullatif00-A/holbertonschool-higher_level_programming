#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    arr = []
    integer = 0
    f = 0.0
    for i in range(0, list_length):
        f = 0
        try:
            f = my_list_1[i] / my_list_2[i]
            integer = 1
        except ZeroDivisionError:
            print("division by 0")
            arr += [0]
        except (TypeError):
            print("wrong type")
            arr += [0]
        except IndexError:
            print("out of range")
            arr += [0]
        finally:
            if integer == 1:
                integer = 0
                arr += [f]
    return arr
