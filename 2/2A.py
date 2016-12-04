fIn = open("input.txt", "r")
lines = fIn.readlines()

def pos2n(pos):
    if pos == (0,0):
        return "1"
    elif pos == (0,1):
        return "4"
    elif pos == (0,2):
        return "7"
    elif pos == (1,0):
        return "2"
    elif pos == (1,1):
        return "5"
    elif pos == (1,2):
        return "8"
    elif pos == (2,0):
        return "3"
    elif pos == (2,1):
        return "6"
    elif pos == (2,2):
        return "9"

def c2pos(c, pos):
    if c == "U":
        if(pos[1] > 0):
            return (pos[0], pos[1] - 1)
        return pos
    elif c == "D":
        if(pos[1] < 2):
            return (pos[0], pos[1] + 1)
        return pos
    elif c == "L":
        if(pos[0] > 0):
            return (pos[0] - 1, pos[1])
        return pos
    elif c == "R":
        if(pos[0] < 2):
            return (pos[0] + 1, pos[1])
        return pos

code = []

cmds = "UDLR"

pos = (1, 1)
for line in lines:
    print(pos)
    for c in line:
        if c in cmds:
            pos = c2pos(c, pos)
    code.append(pos2n(pos))

print "".join(code)

fIn.close()
