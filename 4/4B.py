import string

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

def trns(txt, code):
    s = ""
    add = code % 26
    for c in txt:
        if c.isalpha():
            x = ord(c) + add;
            if(x > 122):
                y = x - 123
                x = 97 + y
            s += chr(x)
        else:
            s += c
    return s

fIn = open("input.txt", "r")
lines = fIn.readlines()

print "Now check manually... in the file output.txt"

for line in lines:
    prt = dec(line)
    cs = chks(clet(prt[0]))
    if cs == prt[2]:
        x = trns(prt[0], prt[1])
        if "northpole" in x:
            print "%s > %s > %s" % (prt[1], prt[0], x) 

fIn.close()    
    
