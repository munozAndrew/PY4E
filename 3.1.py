hrs = input("Enter Hours:")
rte = input("Enter Rate:")
h = float(hrs)
r = float(rte)
max = 0
overTime = 0
overTimePay = 0
totalPay = 0
if h <= 40:
    totalPay = h * r
elif h > 40:
    max = 40 * r
    overTime = h - 40
    overTimePay = r * 1.5
    totalPay = overTime * overTimePay + max
print(totalPay)
