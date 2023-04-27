num = int(input())

#чи є введене число парним
if (num%2):
    print("Odd")
else:
    print("Even")

#чи є число не парним,
#ділиться чи на три і на п'ять одночасно,
#але так, щоб не ділитися на 10
if (not(num%2) and (num%3) and (num%5) and not(num%10)):
    print("Yes")
else:
    print("No")

#вивести усі його дільники
print("Fractors:")

for i in range(1,num//2+1):
    if (not(num%i)):
        print(i)

print(num)

#вивести його розряди та їх множники
print("Degrees:")
i = 0

while (num//10):
    d = num%10
    print(f'{d}*10^{i}', end = " + ")
    i += 1
    num //= 10
d = num%10    
print(f'{d}*10^{i}')
    
