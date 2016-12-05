import hashlib

pwd = ""
chsh = "reyedfim"
i = 0
while len(pwd) < 8:
    hd = hashlib.md5(chsh + str(i)).hexdigest()
    if hd[:5] == "00000":
        pwd += hd[5]
    i += 1
print pwd    
