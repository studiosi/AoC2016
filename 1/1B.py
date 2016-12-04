def turn(h, d):
    if h == "N":
        if d == "L":
            return "W"
        else:
            return "E"        
    elif h == "E":
        if d == "L":
            return "N"
        else:
            return "S"
    elif h == "S":
        if d == "L":
            return "E"
        else:
            return "W"
    elif h == "W":
        if d == "L":
            return "S"
        else:
            return "N"

def move(p, n, h):
    if h == "N":
        return (p[0], p[1] + n)
    elif h == "E":
        return (p[0] + n, p[1])
    elif h == "S":
        return (p[0], p[1] - n)
    elif h == "W":
        return (p[0] - n, p[1])


def travel(instrs):
    heading = "N"
    point = (0, 0)
    pointList = []
    pointList.append(point)
    for instr in instrs:
        d, n = instr[0], int(instr[1:])
        heading = turn(heading, d)
        for i in xrange(n):
            point = move(point, 1, heading)
            if point in pointList:
                return point
            pointList.append(point)

fIn = open("input.txt", "r")
instrs = map( lambda x: x.strip(), "".join(fIn.readlines()).split(",") )

point = travel(instrs)

print abs(point[0]) + abs(point[1])

fIn.close()



    
