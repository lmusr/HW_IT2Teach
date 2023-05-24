def print_prime_squares(nmax):
    p = list(range(nmax+1))
    for i in range(2, int(nmax**0.5)+1):
        if p[i]:
            for j in range(i+i,nmax+1,i):
                if p[j]: p[j] = 0
    print(list(map(lambda x: x*x, filter(lambda x: bool(x), p))))
        
