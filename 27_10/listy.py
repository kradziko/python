l = range(1,21)
print l

l.append(22)
print l

l.extend([20,24])
print l

print "ile 20: ", l.count(20)
print l.index(20)

l.insert(12,44)
print l

l.pop(12)
print l

l.remove(20)
print l
print l.index(20)

l.reverse()
print l

l.sort()
print l