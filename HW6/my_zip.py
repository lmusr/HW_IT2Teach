def my_zip(s1,s2):
    return((s1[i], s2[i]) for i in range(min((len(s1),len(s2)))))

s = 'abcd'
t = (10, 20, 30, 40, 50)

print("my_zip: ", tuple(my_zip(s,t)))
print("zip:    ", tuple(zip(s,t)))
