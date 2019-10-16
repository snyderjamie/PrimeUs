

class Multiply():
    def __init__(self):
        pass


    def two_lists(self, rows, columns):
        'create a multiplication table from two lists of integers'

        table = []
        row1 = ['X']
        row1.extend(columns)
        table.append(row1)
        for row in sorted(rows):
            row_list = [row]
            for column in sorted(columns):
                row_list.append(row * column)
            table.append(row_list)
        return table


    def two_lists_dict(self, rows, columns):
        'create a multiplication table from two lists of integers'

        table = dict()
        for row in sorted(rows):
            row_dict = dict()
            for column in sorted(columns):
                row_dict[column] = row * column
            table[row] = row_dict

        return table


    def format_table(self, table):
        'return a nicely(ish) formatted table'

        # get the width of each column
        widths = []
        for col in zip(*table):
            widths.append(max(map(len, map(str, col))))

        # create the formatted rows
        output_rows = []
        for row in table:
            output_rows.append(' '.join(str(val).rjust(width)
                                        for val, width in zip(row, widths)))

        output = '\n'.join(output_rows)
        return output

