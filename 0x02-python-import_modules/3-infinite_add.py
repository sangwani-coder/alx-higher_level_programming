#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    Sum = 0
    num = sys.argv
    if len(num) <= 1:
        print('0')
    for i in range(len(num) - 1):
        Sum += int(num[i + 1])
    print(Sum)
