#!/usr/bin/python3

import sys
import os

def print_data(data):
    print()
    for i in range(len(data) - 1):
        for j in range(len(data[i]) - 1):
            sys.stdout.write("  %.2f\t" % (data[i][j]))
        sys.stdout.write("|\t%.2f\n" % (data[i][-1]))
        for j in range(len(data[i]) - 1):
            sys.stdout.write(" \t")
        sys.stdout.write("|\n")
    for j in range(len(data[0]) - 1):
        sys.stdout.write("--------")
    sys.stdout.write("+------------\n")
    for j in range(len(data[i]) - 1):
        sys.stdout.write(" \t")
    sys.stdout.write("|\n")
    for j in range(len(data[-1]) - 1):
        sys.stdout.write("  %.2f\t" % (data[-1][j]))
    sys.stdout.write("|\t%.2f\n\n" % (data[-1][-1]))


def swap(data, r, s):
    pivot = data[r][s]
    print("Pivot [%d][%d]: %.2f" % (r, s, pivot))
    new_data = []

    for i in range(len(data)):
        new_row = []
        for j in range(len(data[0])):
            new_row.append(float(0))
        new_data.append(new_row)
    for i in range(len(data)):
        for j in range(len(data[0])):
            new_data[i][j] = 0
            if i == r and j == s:
                new_data[i][j] = 1 / pivot
            if i == r and j != s:
                new_data[i][j] = -1 * data[i][j] / pivot
            if i != r and j == s:
                new_data[i][j] = data[i][j] / pivot
            if i != r and j != s:
                new_data[i][j] = data[i][j] - ((data[r][j] * data[i][s]) / pivot)
    return new_data


def simplex(data):
    r = -1
    s = -1
    q = 0

    for j in range(len(data[0]) - 1):
        print("%d %d %f" % (len(data) - 1, j, data[len(data) - 1][j]))
        if data[len(data) - 1][j] > 0:
            s = j
    if s != -1:
        for i in range(len(data) - 1):
            if data[i][s] < 0:
                temp = data[i][len(data[0]) - 1] / data[i][s]
                print(temp)
                print("data[%d][%d] / data[%d][%d] == %.2f" % (i, len(data[0]) - 1, i, s, temp))
                if q == 0 or q < 0 and temp > q:
                    q = temp
                    r = i
    if r != -1 and s != -1:
        data = swap(data, r, s)
    print()
    print("=" * 50)
    print_data(data)
    return data


def main():

    if len(sys.argv) < 2:
        sys.exit(1)

    input_file = open(sys.argv[1], "r")

    data = []
    temp = input_file.readline().strip().split()
    while len(temp) != 0:
        temp = list(map(float, temp))
        data.append(temp)
        temp = input_file.readline().strip().split()
    print_data(data)

    new_data = simplex(data)
    while new_data != data:
        data = new_data
        input()
        new_data = simplex(data)


if __name__ == '__main__':
    main()
