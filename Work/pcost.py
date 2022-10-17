# pcost.py
#
# Exercise 1.27

import csv
import sys


def portfolio_cost(filename):
    cost_total = 0
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for line in rows:
            try:
                cost_total += int(line[1]) * float(line[2])
            except ValueError:
                print("Can not read this", line)
    return cost_total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input("file path: ")
cost = portfolio_cost(filename)
print('Total cost', cost)
