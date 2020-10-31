import driver

def letter(row, col):
    if col <= 6 and col >= 3 and row >= 2 and row <= 4:
        return 'M'
    else:
        return 'S'

if __name__ == '__main__':
    driver.compare_patterns(letter)
