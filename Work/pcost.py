# pcost.py
#
# Exercise 1.27

import csv
import sys
import report


def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    return sum([item["shares"] * item["price"] for item in portfolio])

    # with open(filename, "rt") as f:
    #     rows = csv.reader(f)
    #     headers = next(rows)
    #     for index, line in enumerate(rows, start=1):
    #         record = dict(zip(headers, line))
    #         try:
    #             cost_total += int(record["shares"]) * float(record["price"])
    #         except ValueError:
    #             print(f"Row {index} Couldn't convert: {line}")
    # return cost_total


if len(sys.argv) == 2:
    filepath = sys.argv[1]
else:
    filepath = input("file path: ")
cost = portfolio_cost(filepath)
# cost = portfolio_cost('Data/portfolio.csv')

print('Total cost', cost)
