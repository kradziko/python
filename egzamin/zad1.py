def a_tergo(nazwa_pliku):
    plik = open(nazwa_pliku,'rb')
    #sprawdzic jak to bylo z with
    na_odwrot = []
    for linia in plik.readlines():
        pom = linia.split()
        for x in pom:
            if x[-1::-1] not in na_odwrot:
                na_odwrot.append((x[-1::-1],1))
            else:
                na_odwrot.append((x[-1::-1], 1))
    print na_odwrot

a_tergo('wyrazy.txt')
