fIn = open("input.txt", "r")
lines = fIn.readlines()

def chabba(s):
    return s[0] == s[2] and s[0] != s[1]

def gprts(s):
    x = s.replace("[", " ").replace("]", " ").split()
    outs, insi = [], []
    for i in xrange(len(x)):
        if i % 2 == 0:
            outs.append(x[i])
        else:
            insi.append(x[i])
    return (outs, insi)

def faba(outs):
    x = []
    for o in outs:
        for i in xrange(len(o) - 2):
            if chabba(o[i:i+3]):
                x.append(o[i:i+3])
    return x

def fbabs(insi, cbabs):
    for o in insi:
        for i in xrange(len(o) - 2):
            if o[i:i+3] in cbabs:
                return True
    return False

def invrs(cabas):
    x = []
    for caba in cabas:
        x.append(invr(caba))
    return x

def invr(s):
    return s[1] + s[0] + s[1]

g = 0
for inp in lines:
    (outs, insi) = gprts(inp)
    cabas = faba(outs)
    if len(cabas) > 0:
        cbabs = invrs(cabas)
        if fbabs(insi, cbabs):
            g = g + 1
print g

fIn.close()
