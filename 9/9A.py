fIn = open("input.txt", "r")
i = "".join(fIn.readlines())

r = ""
x = 0

while x < len(i):
    c = i[x]
    if c == "(":
        x = x + 1
        c = i[x]
        mrk = ""
        while c != ")":
            mrk = mrk + c
            x = x + 1
            c = i[x]
        w = mrk.split("x")
        nc = int(w[0])
        nr = int(w[1])
        rs = ""
        for j in xrange(nc):
            x = x + 1
            rs = rs + i[x]
        for j in xrange(nr):
            r = r + rs
    else:
        r = r + c
    x = x + 1

print len("".join(r.split()))
    
    
        
