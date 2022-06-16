def computepay(h, r):
    if h < 40:
        gp = h*r
    else:
        gp = (40*r) + ((h-40)*1.5*r)
    return (gp)
        
h = input("Enter Hours: ")
r = input("Enter Rate/hour: ")
fh = float(h)
fr = float(r)
gp = computepay(fh, fr)
print("Pay", gp)