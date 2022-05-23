hrs = input("Enter Hours:")
h = float(hrs)
rate = float(input("Enter Rate:"))
if h > 40:
    z = h - 40
    p = 40*rate
    c = z*1.5*rate
    print(p+c)
else:
    print(h*rate)
    