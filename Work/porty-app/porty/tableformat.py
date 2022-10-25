# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print("<tr>", end="")
        for i in headers:
            print(f"<th>{i}</th>", end="")
        print("</tr>", end="")
        print()

    def row(self, rowdata):
        print("<tr>", end="")
        for i in rowdata:
            print(f"<td>{i}</td>", end="")
        print("</tr>", end="")
        print()


class FormatError(Exception):
    pass


def create_formatter(name):
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown format table format {name}')


def print_table(objects, headers, formatter):
    formatter.headings(headers)
    for obj in objects:
        rowdata = [str(getattr(obj, name)) for name in headers]
        formatter.row(rowdata)


