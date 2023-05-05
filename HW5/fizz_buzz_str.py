
fizz, buzz, n = (int(c) for c in input().split(' '))

s = ""
for i in range(1,n+1):
        if i%fizz and i%buzz:
            s += str(i)    
        if not i%fizz:
            s += 'F'
        if not i%buzz:
            s += 'B'
        s += " "

print(s)
    
    

