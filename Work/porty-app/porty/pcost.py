# pcost.py
#
# Exercise 1.27


from . import report


def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    # return sum([item.cost for item in portfolio])
    return portfolio.total_cost

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


def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    print('Total cost:', portfolio_cost(args[1]))


if __name__ == '__main__':
    import sys
    main(sys.argv)

# python pcost.py Data/portfolio.csv
