import finder_funcs

def puzzle_input():
    puzzle_string = input()
    return puzzle_string

def word_input():
    words = input()
    return words.split()


def main():
    puzzle_string = puzzle_input()
    words = word_input()
    rows = finder_funcs.get_rows(puzzle_string)
    print("Puzzle:")
    print("")
    for number in rows:
        print(number)
    print("")
    print(finder_funcs.word(puzzle_string, words))


if __name__ == '__main__':
    main()
