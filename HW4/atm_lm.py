notes = [10, 20, 50, 100, 200, 500, 1000]
sum1 = int(input("sum: "))
i = 0
while (sum1 > 0 and i<len(notes)-1):
    n = 10
    while ((sum1 - n*notes[i])%notes[i+1] or (sum1 - n*notes[i]) < 0):
        n -= 1
    print(notes[i], n)
    sum1 -= notes[i]*n
    i +=1
if (sum1):
    print(notes[i], sum1//notes[i])
    
