#fIn = open("input.txt", "r")
#j = "".join(fIn.readlines())

j = open('input.txt').read().strip()


r = 0

def css(s):
    if "(" not in s:
        return len(s)
    r = 0
    while "(" in s:
        r += s.find("(")
        s = s[s.find("("):]
        m = s[1:s.find(")")].split("x")
        s = s[s.find(")") + 1:]
        r += css(s[:int(m[0])]) * int(m[1])
        s = s[int(m[0]):]
    r += len(s)
    return r

print css(j)

#fIn.close()        
            
    
    
        
