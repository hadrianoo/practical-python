# report.py
#
# Exercise 2.4


from . import fileparse
from . import tableformat
from .portfolio import Portfolio


def read_portfolio(filename, **opts):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        return Portfolio.from_csv(lines, **opts)


def read_prices(filename):
    with open(filename) as file:
        return dict(fileparse.parse_csv(file,
                                        types=[str, float],
                                        has_headers=False))


def make_report(portfolio, prices):
    report = []
    for line in portfolio:
        line = (line.name,
                line.shares,
                prices[line.name],
                prices[line.name] - line.price
                )
        report.append(line)
    return report


def print_report(reportdata, formatter):
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(portfolio_filename, prices_filename, fmt="txt"):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    if 4 < len(args) < 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    if len(args) == 3:
        portfolio_report(args[1], args[2])
    else:
        portfolio_report(args[1], args[2], args[3])


if __name__ == '__main__':
    import sys
    main(sys.argv)


# portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
# python report.py Data/portfolio.csv Data/prices.csv
