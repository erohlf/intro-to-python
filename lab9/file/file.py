def main():
    fl = open('in.txt', 'r')
    line_num = 1
    for line in fl.readlines():
        lst = []
        line2 = line.strip()
        print("Line {0} ({1} chars): {2}".format(line_num, len(line)-1, line, end = ''))
        line_num += 1
    fl.close()
        
if __name__ == '__main__':
    main()
    


