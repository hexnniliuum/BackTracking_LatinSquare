import time

def get_cell(n, row, column):
    return int((row - 1) * (n - 1) + column - 1)

def get_row(cell, n):
    return int(cell / (n - 1) + 1)

def get_column(cell, n):
    return int(cell % (n - 1) + 1)

def forward(i, square, n):
    check = 1
    row = get_row(i, n)
    check = square[i] != row
    if not(check):
        return 0

    #checking row
    column = 1
    cell = get_cell(n, row, column)
    while (cell < i and check):
        check = square[cell] != square[i]
        column = column + 1
        cell = get_cell(n, row, column)

    if not(check):
        return 0

    #checking column
    column = get_column(i, n)
    check = square[i] != column
    if not(check):
        return 0

    row = 1
    cell = get_cell(n, row, column)
    while (cell < i and check):
        check = square[cell] != square[i]
        row = row + 1
        cell = get_cell(n, row, column)

    return check

def LSRec(i, square, n):

    size = (n - 1) * (n - 1)

    if (i < 0 or forward(i, square, n)):
        if (i == size - 1):
            printl(square, n)
        else:
            for num in range(0, n):
                square[i + 1] = num
                LSRec(i + 1, square, n)

def set_up(n):
    if (n <= 1):
        return

    square = [''] * ((n-1)*(n-1))
    return square

def printl(square, n):
    row, col, cell = 0, 0, 0

    for col in range(0, n):
        print(col, end='\t')
    print('\n')
    for row in range(1, n):
        print(row, end='\t')
        for col in range(1, n):
            print(square[cell], end='\t')
            cell = cell + 1
        print('\n')
    print('\n')

def main():
    n = 4

    sq = set_up(n)
    start = time.time()
    LSRec(-1, sq, n)
    print("time: {:.10f}".format(time.time() - start))

if __name__ == '__main__':
    main()
