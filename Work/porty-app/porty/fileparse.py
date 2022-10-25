# fileparse.py
#
# Exercise 3.3

import csv
import logging
log = logging.getLogger(__name__)


def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''

    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers (if any)
    headers = next(rows) if has_headers else []

    # If specific columns have been selected, make indices for filtering
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    records = []
    for index, row in enumerate(rows, start=1):
        if not row:  # Skip rows with no data
            continue

        # If specific column indices are selected, pick them out
        if select:
            row = [row[index] for index in indices]

        # Apply type conversion to the row
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning("Row %d: Couldn't convert %s", index, row)
                    log.debug("Row %d: Reason %s", index, e)
                continue

        # Make a dictionary or a tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records


# prices = parse_csv('Data/prices.csv', types=[str, float], has_headers=False)
# prices = parse_csv('Data/missing.csv', types=[str, int, float], silence_errors=False)
# print(prices)