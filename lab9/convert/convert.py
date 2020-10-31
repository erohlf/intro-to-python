def float_default(val, flt):
    try:
        float(val)
        return val
    except ValueError:
        return flt
