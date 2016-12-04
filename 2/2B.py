fIn = open("input.txt", "r")
lines = fIn.readlines()

def pos2n(pos):
    if pos == (2,0):
        return "1"
    elif pos == (1,1):
        return "2"
    elif pos == (2,1):
        return "3"
    elif pos == (3,1):
        return "4"
    elif pos == (0,2):
        return "5"
    elif pos == (1,2):
        return "6"
    elif pos == (2,2):
        return "7"
    elif pos == (3,2):
        return "8"
    elif pos == (4,2):
        return "9"
    elif pos == (1,3):
        return "A"
    elif pos == (2,3):
        return "B"
    elif pos == (3,3):
        return "C"
    elif pos == (2,4):
        return "D"

def c2pos(c, pos):
    if c == "U":
        return (pos[0], pos[1] - 1)
    elif c == "D":
        return (pos[0], pos[1] + 1)
    elif c == "L":
        return (pos[0] - 1, pos[1])
    elif c == "R":
        return (pos[0] + 1, pos[1])

alcmds = {
    (2,0) : "D",
    (1,1) : "RD",
    (2,1) : "UDLR",
    (3,1) : "DL",
    (0,2) : "R",
    (1,2) : "UDLR",
    (2,2) : "UDLR",
    (3,2) : "UDLR",
    (4,2) : "L",
    (1,3) : "UR",
    (2,3) : "UDLR",
    (3,3) : "UL",
    (2,4) : "U"
}

code = []
pos = (0, 2)
for line in lines:
    for c in line:
        if c in alcmds[pos]:
            pos = c2pos(c, pos)
    code.append(pos2n(pos))

print "".join(code)
fIn.close()
