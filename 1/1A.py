def turn(d):
    if heading == "N":
        if d == "L":
            return "W"
        else:
            return "E"        
    elif heading == "E":
        if d == "L":
            return "N"
        else:
            return "S"
    elif heading == "S":
        if d == "L":
            return "E"
        else:
            return "W"
    elif heading == "W":
        if d == "L":
            return "S"
        else:
            return "N"

def move(p, n):
    if heading == "N":
        return (p[0], p[1] + n)
    elif heading == "E":
        return (p[0] + n, p[1])
    elif heading == "S":
        return (p[0], p[1] - n)
    elif heading == "W":
        return (p[0] - n, p[1])

fIn = open("input.txt", "r")
instrs = map( lambda x: x.strip(), "".join(fIn.readlines()).split(",") )

heading = "N"
point = (0, 0)

for instr in instrs:
    d, n = instr[0], int(instr[1:])
    heading = turn(d)
    point = move(point, n)

print abs(point[0]) + abs(point[1])
