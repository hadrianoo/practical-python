# report.py
#
# Exercise 2.4

import csv
import locale


def read_portfolio(filename):
    with open(filename, "rt") as f:
        portfolio = []
        rows = csv.reader(f)
        headers = next(rows)
        for name, shares, price in rows:
            row = {"name": name, "shares": int(shares), "price": float(price)}
            portfolio.append(row)
    return portfolio


def read_prices(filename):
    with open(filename, "rt") as f:
        prices = {}
        rows = csv.reader(f)
        for data in rows:
            try:
                prices[data[0]] = float(data[1])
            except IndexError:
                pass
    return prices


# def current_price(filename1, filename2):
#     prices = read_prices(filename1)
#     portfolio = read_portfolio(filename2)
#
#     total_cost = 0.0
#     for s in portfolio:
#         total_cost += s['shares'] * s['price']
#     print('Total cost', total_cost)
#
#     total_value = 0.0
#     for s in portfolio:
#
#         total_value += s['shares'] * prices[s['name']]
#
#     print('Current value', total_value)
#     print('Gain', total_value - total_cost)
#
# current_price("data/prices.csv", "data/portfolio.csv")


def make_report(portfolio, prices):
    report = []
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    for line in portfolio:
        line = (line["name"], line["shares"], prices[line["name"]], prices[line["name"]] - line["price"])
        report.append(line)
    return report


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print(f"{headers[0]:>10s}{headers[1]:>10s}{headers[2]:>10s}{headers[3]:>10s}")
print('---------- --------- --------- ----------')
for name, shares, price, change in report:
    print(f"{name:>10s}{shares:>10d}{price:>10.2f}{change:>10.2f}")

