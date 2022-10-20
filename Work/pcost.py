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
        for index, line in enumerate(rows, start=1):
            record = dict(zip(headers, line))
            try:
                cost_total += int(record["shares"]) * float(record["price"])
            except ValueError:
                print(f"Row {index} Couldn't convert: {line}")
    return cost_total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input("file path: ")
cost = portfolio_cost(filename)
print('Total cost', cost)
