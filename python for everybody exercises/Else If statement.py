rate = input("Enter Rate:")
hrs = input("Enter hours worked below 40")
Question = input("did you work more than 40 hours?")
if Question == "yes":
    ot = float(input("Enter Hours: worked above 40"))

fr = float(rate)
fh = float(hrs)


def computepay():
    ot_rate = 1.50
    overtime = ot * ot_rate
    return float(fh + overtime) * fr


p = computepay()
print("Pay", p)
