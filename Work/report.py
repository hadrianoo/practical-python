# report.py
#
# Exercise 2.4


import fileparse


def read_portfolio(filename):
    return fileparse.parse_csv(filename,
                               select=["name", "shares", "price"],
                               types=[str, int, float])
    # with open(filename, "rt") as f:
    #     portfolio = []
    #     rows = csv.reader(f)
    #     headers = next(rows)
    #     for row in rows:
    #         record = dict(zip(headers, row))
    #         new_row = {"name": record["name"],
    #                    "shares": int(record["shares"]),
    #                    "price": float(record["price"])
    #                    }
    #         portfolio.append(new_row)
    # return portfolio


def read_prices(filename):
    return dict(fileparse.parse_csv(filename,
                                    types=[str, float],
                                    has_headers=False))
    # with open(filename, "rt") as f:
    #     prices = {}
    #     rows = csv.reader(f)
    #     for data in rows:
    #         try:
    #             prices[data[0]] = float(data[1])
    #         except IndexError:
    #             pass
    # return dict(prices)


def make_report(portfolio, prices):
    report = []
    for line in portfolio:
        line = (line["name"],
                line["shares"],
                prices[line["name"]],
                prices[line["name"]] - line["price"]
                )
        report.append(line)
    return report


def print_report(reportdata):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f"{headers[0]:>10s}{headers[1]:>10s}{headers[2]:>10s}{headers[3]:>10s}")
    print('---------- --------- --------- ----------')
    for name, shares, price, change in reportdata:
        print(f"{name:>10s}{shares:>10d}{price:>10.2f}{change:>10.2f}")


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
