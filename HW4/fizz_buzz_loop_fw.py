import sys

fn_input = sys.argv[1]
fn_output = sys.argv[2]
fin = open(fn_input, 'r')
fout = open(fn_output, 'w')

for line in fin: # для кожного рядка у файлі

    fizz, buzz, n = (int(s) for s in line.split(' '))

    for i in range(1,n+1):
        if not i%fizz and not i%buzz:
            fout.write('FB ')    
        elif not i%fizz:
            fout.write('F ')
        elif not i%buzz:
            fout.write('B ')
        else:
            fout.write(str(i)+' ')
    fout.write("\n")

fin.close() 
fout.close()
