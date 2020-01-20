def computepay(h,r):
    if (h > 40):
        rp = h * r
        ot = (h - 40) * (r * 0.5)
        pay = rp + ot
    else:
        pay = h * r
    return pay

hrs = input("Enter Hours:")
rph = input("Enter Rate per Hour:")

h = float(hrs)
r = float(rph)

comppay = computepay(h,r)
print("Pay", comppay)
