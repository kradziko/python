'''
Tabliczka mnozenia zapisana do pliku
'''
f1 = open("plik1.txt","wb")
for i in range(1,11):
    for j in range(1,11):
        f1.write ("%-3i" % (i*j),)
    f1.write("\n")