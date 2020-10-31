def group_pixels(fil):
    ifile = open(fil, 'r')
    ifil.readline()
    ifil.readline()
    ifil.readline()
    lst = []
    for line in ifil:
        ifil.readline()
        line2 = line.split()
        while len(lst) < 9:
            lst.append(line2[0:-1])
            lst.append(line2[-1])
    ifile.close()
    return lst 


