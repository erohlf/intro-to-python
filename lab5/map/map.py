def square_all(list1):
    squarelist = []
    count = 0
    while count < len(list1):
        square = list1[count] ** 2
        squarelist.append(square)
        count += 1
    return squarelist
    
def add_n_all(list1, n):
    addn = []
    for count in list1:
        add = count + n
        addn.append(add)
    return addn

def even_or_odd_all(list1):
    return [num % 2 == 0  for num in list1] 
