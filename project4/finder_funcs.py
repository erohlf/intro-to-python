# Name:        Ethan Rohlf
# Course:      CPE 101
# Instructor:  Nupur Garg
# Assignment:  Project4
# Term:        Spring 2017



def get_rows(puzzle_string):
    rows = []
    for number in range(10):
        rows2 = []
        for num in range(10):
            rows2.append(puzzle_string[num + (10 * number)])
        rows2 =''.join(rows2)
        rows.append(rows2)
    return rows

def get_columns(puzzle_string):
    columns = []
    for number in range(10):
        columns2 = []
        for num in range(0, 100, 10):
            columns2.append(puzzle_string[number + num])
        columns2 = ''.join(columns2)
        columns.append(columns2)
    return columns


def backwards_string(string):
    number  = len(string) - 1
    reverse_string = []
    while number >= 0:
        reverse_string.append(string[number])
        number -= 1
    return ''.join(reverse_string)


def word_in_rows(puzzle, word):
    rows = get_rows(puzzle)
    for number in range(10):
       row_number = rows[number]
       try:
           column = int(rows[number].index(word[0]))   #This code only works when the first letter of the word has its first occurance in each row at the start of the word. I solved this problem using .find(), but didn't include it because you said we couldn't use things you haven't told us.        
       except ValueError:
           pass
       if word  in row_number:
           return("{0}: (FORWARD) row: {1} column: {2}".format(word, number, column))
       else:
           backwards_row = backwards_string(rows[number])
           try:
               column = int(rows[number].index(word[0]))
           except ValueError:
               pass
           if word in backwards_row:
               return("{0}: (BACKWARD) row: {1} column: {2}".format(word, number, column))
    return False

def word_in_columns(puzzle, word):
    columns = get_columns(puzzle)
    for number in range(10):
       col_number = columns[number]
       try:
           row = int(columns[number].index(word[0]))
       except ValueError:
           pass
       if word in col_number:
           return("{0}: (DOWN) row: {1} column: {2}".format(word, row, number))
       else:
           backwards_col = backwards_string(columns[number])
           try:
               row = int(columns[number].index(word[0]))
           except ValueError:
               pass
           if word in backwards_col:
               return("{0}: (UP) row: {1} column: {2}".format(word, row, number))    
    return False


def word(puzzle, words):
    solution = []
    for number in range(len(words)):
        rows = word_in_rows(puzzle, words[number])
        columns = word_in_columns(puzzle, words[number])
        if columns == False and rows == False:
            solution.append("{0}: word not found".format(words[number]))
        elif columns != False:
            solution.append(columns)
        elif rows != False:
            solution.append(rows)
    for count in solution:
        print(count)
    return ''


        



