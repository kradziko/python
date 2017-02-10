'''napisz jednolinijkowa funkcje zwracajaca liste dzielnikow dodatnich argumentu bedacego liczba dodatnia'''

def dzielniki(n):
    return filter(lambda x: not (n%x),range(1,n))

print dzielniki(128)



