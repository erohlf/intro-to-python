import driver

def letter(row, col):
    if row == 9 and col == 9:
        return 'Z'
    return 'G'

if __name__ == '__main__':
    driver.compare_patterns(letter)
