#!/usr/bin/python3
def uppercase(str):
    result = ''
    for i in str:
        if ord(i) >= 97 and ord(i) < 123:
            result = result + chr(ord(i) - 32)
        else:
            result = result + i
    print('{}'.format(result))
