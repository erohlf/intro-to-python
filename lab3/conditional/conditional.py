def max_101(x, y):
    if x > y:
        return x
    elif y > x:
        return y

def max_of_three(x, y, z):
    x = float(x)
    y = float(y)
    z = float(z)
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z
    else:
        return x

def rental_late_fee(x):
    x = int(x)
    if x <= 0:
        return 0
    elif x <= 9:
        return 5
    elif x <= 15:
        return 7
    elif x <= 24:
        return 19
    else:
        return 100

