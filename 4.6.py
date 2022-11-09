def computepay(h, r):
    if h <= 40:
        totalPay = h * r
    elif h > 40:
        max = 40 * r
        overTime = h - 40
        overTimePay = r * 1.5
        totalPay = overTime * overTimePay + max
    return totalPay
hrs = input("Enter Hours:")
rte = input("Enter Rate:")
h = float(hrs)
r = float(rte)
p = computepay(h, r)
max = 0
overTime = 0
overTimePay = 0
totalPay = 0
print("Pay", p)
