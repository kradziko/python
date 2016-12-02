"""
operacje na plikach i katalogach
"""

from os import *

# sprawedzenie w jakim aktualnie katalogu jestesmy

print getcwd()

# zmiana biezacego katalogu na inny
#chdir('../1_12')
print getcwd()

# zawartosc katalogu
print listdir('..') # . - bierzacy katalog , .. -ktalog wyzej

# zawartosc katalogu - siezka absolutna
print listdir(r'/home/kradziko')

# filtrowanie plikow i katalogow wg okreslonego wzorca

import fnmatch

print fnmatch.fnmatch('Python', 'P*n')
print fnmatch.fnmatch('Python', 'P*e')

# lista plikow z roszerzeniem py
print [x for x in listdir(r'/home/kradziko')
       if fnmatch.fnmatch(x, '*.py')]

# listy plikow konczacych sie liczba '6' lub '1'
print [x for x in listdir(r'/home/kradziko')
       if fnmatch.fnmatch(x, '*[61].*')]

import glob

for x in glob.glob(r'/home/kradziko/*[61].*'):
    print x

# rozdzielenie sciezki absolutnej na katalog w ktorym znajduje sie plik
# oraz nazwe pliku
print path.split('/home/kradziko/test.py')

for x in glob.glob(r'home/kradziko/*[61].*'):
    print path.split(x)[1]

# laczenie ciagu kataogow w sciezke
print path.join('/', 'home', 'kradziko', 'Dokumenty')
print path.join(r'/home', 'kradziko', 'test.py')

# sprawdzenie czy podana sciezka jest absolutna
print path.isabs(r'../script25.py')
print path.isabs(r'/home/kradziko')

# sprawedzenie czy dany obiekt dyskowy istnieje
print path.exists(r'/home/kradziko/')
print path.exists(r'/home/kradziko/test288.py')

# zmiana nazwy katalogu lub pliku
# rename('../Test', '../nTest')
print path.exists('nTest')
print listdir('.')

# sprawdzenie czy dany obiekt dyskowy jest plikiem
print path.isfile('pliki_i_katalogi.py')
print path.isfile('/home')

# sprawedzenie czy dany obiekt dyskowy jest katalogiem
print path.isdir('/home')
print path.isdir('/home/kradziko/.vimrc')

# sprawedzenie czy dany obiekt dyskowy jest dyskiem
print path.ismount('/home')
print path.ismount('/')

# sprawdzenie dlugosci pliku (bajty)
print path.getsize('/home/kradziko/test.py')
print path.getsize('.')

for x in listdir('.'):
    print x, path.getsize(x)

# czas stworzenia pliku
from time import ctime

print ctime(path.getctime('pliki_i_katalogi.py'))

# czas ostatniej modyfikacji
print ctime(path.getctime('pliki_i_katalogi.py'))

# rekursywne przechodzenie katalogow
for sciezka, podkatalogi, pliki in walk(r'/home/kradziko/PycharmProjects/python/10_11'):
    print 'W katalogu %s znajduje sie %i bajtow w %i plikach' \
    % (sciezka, sum(path.getsize(path.join(sciezka, nazwa))
                    for nazwa in pliki), len(pliki))
