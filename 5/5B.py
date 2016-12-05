import hashlib

pwd = ["-", "-", "-", "-", "-", "-", "-", "-"]
vpos = "01234567"
chsh = "reyedfim"
i = 0
while "-" in pwd:
    hd = hashlib.md5(chsh + str(i)).hexdigest()
    if hd[:5] == "00000" and hd[5] in vpos:
        pos = int(hd[5])
        print pos
        if pwd[pos] == "-":
            pwd[pos] = hd[6]
        print pwd
    i += 1
print "".join(pwd)    
