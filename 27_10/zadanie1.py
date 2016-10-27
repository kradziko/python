'''
napisz skrypt ktory znajdzie i wyswietli pozycje na liscie pierwszego wystapienia okreslonej liczby
'''

def znajdz_w_liscie (lista,liczba):
    return lista.index(liczba)

l = [12,45,2,3,5,2,4]
print znajdz_w_liscie(l,2)