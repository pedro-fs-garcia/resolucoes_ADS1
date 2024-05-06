l = [1, 2, 2, 3, 2, 2, 4]

f = (0,0)
for i in set(l):
    freq = l.count(i)
    if freq > f[1]:
        f=(i, l.count(i))


print(f[0])