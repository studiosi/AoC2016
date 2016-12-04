fIn = open("input.txt", "r")
lines = fIn.readlines()

def valid(t):
    return t[1] + t[2] > t[0] and t[0] + t[2] > t[1] and t[0] + t[1] > t[2]

i = 0
j = 0
while j < len(lines):
    
    l1 = map(lambda x: int(x), lines[j].split())
    l2 = map(lambda x: int(x), lines[j+1].split())
    l3 = map(lambda x: int(x), lines[j+2].split())

    if(valid((l1[0], l2[0], l3[0]))):
        i += 1
    if(valid((l1[1], l2[1], l3[1]))):
        i += 1
    if(valid((l1[2], l2[2], l3[2]))):
        i += 1

    j += 3

print i

fIn.close()
