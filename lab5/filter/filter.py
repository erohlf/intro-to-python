def are_positive(list1):
    count = 0
    while count < len(list1):
        if list1[count] < 0:
            list1.remove(list1[count])
        count += 1
    return list1

def are_greater_than_n(list1, n):
    aregreater = []
    for count in list1:
        if count > n:
            aregreater.append(count)
    return aregreater

def are_divisible_by_n(list1, n):
    return [count for count in list1 if count % n == 0]
