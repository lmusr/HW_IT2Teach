notes = [1000, 500, 200, 100, 50, 20, 10]
sum1 = int(input("sum: "))
i = 0
while (sum1 > 0):
    n = sum1//notes[i]
    if (n):
        print(notes[i], n)
    sum1 %= notes[i]
    i += 1
