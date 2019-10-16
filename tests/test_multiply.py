from PrimeUs.Multiply import Multiply


def test_init():
    multiply = Multiply()
    assert type(multiply) is Multiply


def test_two_lists():
    multiply = Multiply()

    rows = [2, 3, 4]
    cols = [5, 6, 7, 8]

    table = multiply.two_lists(rows, cols)

    assert table[1][1] == 10
    assert table[2][2] == 18
    assert table[3][4] == 32


def test_two_lists_dict():
    multiply = Multiply()

    rows = [2, 3, 4]
    cols = [5, 6, 7, 8]

    table = multiply.two_lists_dict(rows, cols)

    assert table[2][5] == 10
    assert table[3][6] == 18
    assert table[4][8] == 32


def test_format_table():
    multiply = Multiply()

    rows = [2, 3, 4, 11, 12]
    cols = [5, 6, 7, 8, 11, 12]

    table = multiply.two_lists(rows, cols)
    chk = multiply.format_table(table)

    assert chk == ' X  5  6  7  8  11  12\n' + \
                  ' 2 10 12 14 16  22  24\n' + \
                  ' 3 15 18 21 24  33  36\n' + \
                  ' 4 20 24 28 32  44  48\n' + \
                  '11 55 66 77 88 121 132\n' + \
                  '12 60 72 84 96 132 144'
