class R:
    def __init__(self):
        self.chps = []

    def recv(self, chp):
        self.chps.append(chp)

    def give(self, r, chp):
        if chp in self.chps:
            self.chps.remove(chp)
            r.recv(chp)

    def gmin(self, r):
        chp = min(self.chps)
        self.give(r, chp)
        return chp

    def gmax(self, r):
        chp = max(self.chps)
        self.give(r, chp)
        return chp

    def ready(self):
        return len(self.chps) >= 2

    def __str__(self):
        x = "R ----\r\n"
        x += "chps: " + str(self.chps) + "\r\n"
        x += "------\r\n"
        return x


def deco(i):
    ip = i.split()
    if ip[0] == "value":
        # (i, value, bot)
        return "RECV", int(ip[1]), ip[5]
    elif ip[2] == "gives":
        # (i, bot, low, high)
        x1 = ""
        if ip[5] == "output":
            x1 = "O"
        x2 = ""
        if ip[10] == "output":
            x2 = "O"
        return "GIVE", ip[1], x1 + ip[6], x2 + ip[11]


def exc(inst, rbts, outs):
    if inst[0] == "RECV":
        if inst[2] not in rbts.keys():
            rbts[inst[2]] = R()
        rbts[inst[2]].recv(inst[1])
    if inst[0] == "GIVE":
        minn, maxn = -1, -1
        if inst[2][0] == "O":
            minn = rbts[inst[1]].gmin(outs[inst[2][1:]])
        else:
            minn = rbts[inst[1]].gmin(rbts[inst[2]])
        if inst[3][0] == "O":
            maxn = rbts[inst[1]].gmin(outs[inst[3][1:]])
        else:
            maxn = rbts[inst[1]].gmax(rbts[inst[3]])
        if minn == 17 and maxn == 61:
            print inst[1]

def crea(key, rbts, outs):
    if key[0] == "O" and key[1:] not in outs:
        rk = key[1:]
        outs[rk] = R()
    if key[0] != "O" and key not in rbts:
        rbts[key] = R()


rbts = {}
istcks = {}
outs = {}

fIn = open("input.txt", "r")
lines = fIn.readlines()

ins = []
for l in lines:
    ins.append(deco(l.strip()))

while len(ins) > 0:
    s = ins.pop(0)
    if s[0] == "RECV":
        exc(s, rbts, outs)
    elif s[0] == "GIVE":
        crea(s[1], rbts, outs)
        crea(s[2], rbts, outs)
        crea(s[3], rbts, outs)
        if rbts[s[1]].ready():

            exc(s, rbts, outs)
        else:
            ins.append(s)

