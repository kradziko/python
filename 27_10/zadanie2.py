'''NWD, NWW'''

def NWD(a,b):
    while(a !=b):
        if (a >b):
            a = a -b
        else:
            b = b - a
    return a

def NWW(a,b):
    return a/NWD(a,b)*b

print NWD(125,45)
print NWW(42,56)
