def computepay(h, r):
    if h > 40:
        p = 1.5 * r * (h - 40) + (40 * r)
    else:
        p = h * r
    return p


hrs = input("Enter Hours:")
hr = float(hrs)
hh = input("Enter rate per hour:")
pp = float(hh)

p = computepay(hr, pp)
