a=2
x=float(input("x = "))
y=float(input("y = "))
if (x < 0) and (y > 0) and (y < x + a/2):
    print("1")
if (x > 0) and (y > 0) and (y < -x + a/2):
    print("2")
if (x > -a/2) and (x < 0) and (y < 0) and (y > -a/2) and (x**2 + (y + a/2)**2 > (a/2)**2):
    print("3")
if (x < 0) and (y > -a/2) and (x**2 + (y + a/2)**2 < (a/2)**2):
    print("4")
if (x > 0) and (y > x - a/2) and (x**2 + (y + a/2)**2 < (a/2)**2):
    print("5")
if (x > 0) and (y < 0) and (y > x - a/2) and (x**2 + (y + a/2)**2 > (a/2)**2):
    print("6")
if (x < a/2) and (y > -a/2) and (y < x - a/2) and (x**2 + (y + a/2)**2 > (a/2)**2):
    print("7")
if (y > -a/2) and (y < x - a/2) and (x**2 + (y + a/2)**2 < (a/2)**2):
    print("8")
if (x > 0) and (y < -a/2) and (x**2 + (y + a/2)**2 < (a/2)**2):
    print("9")
if (x > 0) and (x < a/2) and (y < -a/2) and (y > -a) and (x**2 + (y + a/2)**2 > (a/2)**2):
    print("10")
if (x < 0) and (y < x - a/2) and (x**2 + (y + a/2)**2 < (a/2)**2):
    print("11")
if (y < -a/2) and (y > x - a/2) and (x**2 + (y + a/2)**2 < (a/2)**2):
    print("12")
if (x > -a/2) and (y < -a/2) and (y > x - a/2) and (x**2 + (y + a/2)**2 > (a/2)**2):
    print("13")
if (x < 0) and (y < x - a/2) and (x**2 + (y + a/2)**2 < (a/2)**2):
    print("14")
print("By!")
