# Name:
# Course:
# Instructor:
# Assignment:
# Term:

def main():
    table_size = get_table_size()
    while table_size != 0:
        first = get_first()
        increment = get_increment()
        show_table(table_size, first, increment)
        table_size = get_table_size()
        

# Obtain a valid table size from the user.
def get_table_size():
    size = int(input("Enter number of rows in table (0 to end): "))

    while size < 0:
        print("Size must be non-negative.")
        size = int(input("Enter number of rows in table (0 to end): "))

    return size

# TODO: Enhancement 1 - Add input validation to this function.
# Obtain the first table entry from the user.
def get_first():
    first = int(input("Enter the value of the first number in the table: "))    
    while first < 0:
        print("First number must be non-negative.")
        first = int(input("Enter the value of the first number in the table: "))
    return first

# Display the table of cubes.
def show_table(size, first, increment):
    print("A cube table of size {:d} will appear here starting with {:d}.".format(size, first))
    print("Number  Cube")


    # TODO: Enhancement 2 - Insert loop here.
    total = 0
    for count in range(size):
        print("{:<6d}  {:d}".format(first, first ** 3))
        total += first ** 3
        first = first + increment
    print("The sum of the cubes is: {0}".format(total))

def get_increment():
    increment = int(input("Enter the increment between the rows: ")) 
    while increment < 0:
        print("Increment must be non-negative.")
        increment = int(input("Enter the increment between the rows: ")) 
    return increment

if __name__ == "__main__":
    main()
