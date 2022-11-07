sh = input("Enter hours: ")
sr = input("Enter rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter Numeric input")
    quit()

print(fh, fr)
if fh > 40:
    reg = fr * fh
    otp = (fh - 40) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print("Pay:", xp)