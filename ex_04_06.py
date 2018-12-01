def computepay(hours, rate):
    print("Computing", hours, rate)
    if hours > 40:
        pay1 = (float(hours) - 40.0)* (float(rate) * 0.5)
        pay2 = float(hours)* float(rate)
        pay = pay1 + pay2
        print(xp)
    else:
        pay = float(hours)* float(rate)
    print("Returning", pay)
    return pay

hx = input('Enter hours: ')
rx = input('Enter rate: ')
nhx = float(hx)
nrx = float(rx)
computepay(nhx, nrx)


print("Pay:", pay)
