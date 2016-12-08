import sys

MX = 60
MY = 6

scr = [ [ 0 for x in xrange(MX) ] for y in xrange(MY) ]

def prscr(scr):
    for l in scr:
        for e in l:
            sys.stdout.write(str(e))
        sys.stdout.write('\n')

def sets(scr, x, y):
    scr[y][x] = 1

def uset(scr, x, y):
    scr[x][y] = 0
    
def rect(scr, x, y):
    for ix in xrange(x):
        for iy in xrange(y):
            sets(scr, ix, iy)

def pnot(scr, x, y):
    if scr[y][x] == 1:
        scr[y][x] = 0
    else:
        scr[y][x] = 1

def rotrl(scr, y):
    col = []
    for ix in xrange(MX):
        col.append(scr[y][ix])
    col = col[len(col)-1:] + col[:len(col)-1]
    for ix in xrange(MX):
        scr[y][ix] = col[ix]

def rotrln(scr, y, n):
    for i in xrange(n):
        rotrl(scr, y)

def rotrc(scr, x):
    col = []
    for iy in xrange(MY):
        col.append(scr[iy][x])
    col = col[len(col)-1:] + col[:len(col)-1]
    for iy in xrange(MY):
        scr[iy][x] = col[iy]

def rotrcn(scr, x, n):
    for i in xrange(n):
        rotrc(scr, x)

def coun(scr):
    x = 0
    for ix in xrange(MX):
        for iy in xrange(MY):
            print (ix, iy)
            if scr[iy][ix] == 1:
                x = x + 1
    return x

fIn = open("input.txt", "r")
lines = fIn.readlines()

#lines = ["rect 3x2", "rotate column x=1 by 1", "rotate row y=0 by 4", "rotate column x=1 by 1"]

for line in lines:
    l = line.split()
    if l[0] == "rotate":
        s = l[2].split("=")
        if s[0] == "y":
            rotrln(scr, int(s[1]), int(l[4]))
        elif s[0] == "x":
            rotrcn(scr, int(s[1]), int(l[4]))
    elif l[0] == "rect":
        s = l[1].split("x")
        rect(scr, int(s[0]), int(s[1]))
y = coun(scr)
print y

fIn.close()
