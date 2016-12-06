fIn = open("input.txt", "r")
lines = fIn.readlines()

r = ""
l = len(lines[0])
for i in xrange(l):
    a = {}
    for line in lines:
        c = line[i]
        if c not in a.keys():
            a[c] = 1
        else:
            a[c] = a[c] + 1
    r += max(a, key=lambda k: a[k])

print r

fIn.close()
