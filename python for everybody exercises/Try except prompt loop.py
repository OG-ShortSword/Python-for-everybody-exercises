largest = None
smallest = None
while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        ival = int(sval)
        if largest is None:
            largest = ival
        elif largest < ival:
            largest = ival
        if smallest is None:
            smallest =ival
        elif smallest > ival:
            smallest = ival
    except:
        print('Invalid input')
        continue

print("Maximum is", largest)
print('Minimum is', smallest)