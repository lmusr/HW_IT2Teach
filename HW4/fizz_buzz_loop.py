import sys

filename = sys.argv[1]
f = open(filename, 'r')

for line in f: # для кожного рядка у файлі

    fizz, buzz, n = (int(s) for s in line.split(' '))

    for i in range(1,n+1):
        if not i%fizz and not i%buzz:
            print('FB', end = ' ')    
        elif not i%fizz:
            print('F', end = ' ')
        elif not i%buzz:
            print('B', end = ' ')
        else:
            print(i, end = ' ')
    print()

f.close() 
