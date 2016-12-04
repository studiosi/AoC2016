fIn = open("input.txt", "r")
lines = fIn.readlines()

def valid(t):
    return t[1] + t[2] > t[0] and t[0] + t[2] > t[1] and t[0] + t[1] > t[2]

i = 0
for line in lines:
    t = map(lambda x: int(x), line.split())
    if valid(t):
        i += 1

print i

fIn.close()
