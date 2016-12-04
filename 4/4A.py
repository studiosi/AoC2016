def dec(n):
    chsum = n.split("[")[1].replace("]", "").strip()
    r = n.split("-")
    code = "".join(r[:-1])
    sect = int(r[-1].split("[")[0])
    return (code, sect, chsum)

def clet(code):
    ks = set(code)
    r = {}
    for k in ks:
        r[k] = code.count(k)
    return sorted(r.items(), key = lambda x: x[1], reverse=True)

def chks(scode):
    d = {}
    for t in scode:
        if t[1] not in d.keys():
            d[t[1]] = [t[0]]
        else:
            d[t[1]].append(t[0])
    sks = sorted(d.keys(), reverse=True)
    r = ""
    for k in sks:
        r += "".join(sorted(d[k]))
    return r[:5]

fIn = open("input.txt", "r")
lines = fIn.readlines()

x = 0
for line in lines:
    prt = dec(line)
    cs = chks(clet(prt[0]))   
    if cs == prt[2]:
        x += prt[1]
print x

fIn.close()    
    
