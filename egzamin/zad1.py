# -*- coding: utf-8 -*-
def a_tergo(nazwa_pliku):
    plik = open(nazwa_pliku,'rb')
    #sprawdzic jak to bylo z with
    na_odwrot = []
    for linia in plik:
        pom = linia.split()
        for x in pom:
            for y in na_odwrot:
                if x[-1::-1] in y[0]:
                    y[1] += 1
                    break
            else:
                na_odwrot.append([x[-1::-1], 1])
    print sorted(na_odwrot)

a_tergo('wyrazy.txt')
