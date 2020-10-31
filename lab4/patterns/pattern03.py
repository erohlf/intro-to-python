import driver

def letter(row, col):
    if col >=0 and col <=9:
        return 'X'
    else:
        return 'O'

if __name__ == '__main__':
    driver.compare_patterns(letter)
