#zbiory zmienne

A= set([1,2,3])
print A

#dodawanie i usuwanie elementu ze zbioru
A.discard(3) #usuwanie elementu 3
print A

A.add(8)
print A

B=frozenset([3,5,6])
print B

slownik = {B: 9}
print slownik

C=set([5,4,9])
C.add(B)
print C

D = set()
print D

print len(A), len(B), len(C), len(D)
print '\n'
print 5 in A, 5 in B, 5 in C, 5 in D
#sprawdzanie czy obiekt nie jest elementem zbioru
print 8 not in A, 8 not in B, 8 not in C, 8 not in D
print '\n'
#sprawdzanie czy dany zbior jest podzbiorem innego zbioru
print set([1,2]) <= A
print set([3,4]) <= B
print set([5]) <= B
print set([1,3,5]) <=A
print '\n'
print A.issubset(B)
print '\n'
#sprawdzanie czy dany zbior jest nadzbiorem innego wzoru
print A >= set([1,2])
print B >=set([3,4])

print A.issuperset(B)
print '\n'

#laczenie zbiorow
print "A" , A
print "B", B
E=A | B
print E
print '\n'

F = A & B
print F
print '\n'

print "A-B",A-B
print "B-A", A-B
print '\n'

G=A^B
print "G", G
