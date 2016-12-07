fIn = open("input.txt", "r")
lines = fIn.readlines()

def chabba(s):
    return s[0] == s[3] and s[1] == s[2] and s[0] != s[1]

def gprts(s):
    x = s.replace("[", " ").replace("]", " ").split()
    outs, insi = [], []
    for i in xrange(len(x)):
        if i % 2 == 0:
            outs.append(x[i])
        else:
            insi.append(x[i])
    return (outs, insi)

g = 0
for inp in lines:
    (outs, insi) = gprts(inp)
    good = False
    for k in outs:
        for i in xrange(len(k) - 3):
            if chabba(k[i:i+4]):
                good = True
    for k in insi:
        for i in xrange(len(k) - 3):
            if chabba(k[i:i+4]):
                good = False
    if good:
        g += 1
print g
fIn.close()
