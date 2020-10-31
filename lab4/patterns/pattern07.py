import driver

def letter(row, col):
    if (row >= 2 and row <= 5 ) and (col <= 9 and col >= 4):
        if (row >= 4 and row <= 5) and (col <=9 and col >=7):
            return 'X'
        return 'Z'
    if (row >= 4 and row <= 6) and (col <= 12 and col >= 7):
        return 'B'
    else:
        return 'T'


if __name__ == '__main__':
    driver.compare_patterns(letter)
