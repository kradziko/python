'''rekordy'''

class Adres:
    pass

adr1 = Adres()
adr1.ulica = 'stonogi'
adr1.nr = 23
adr1.kod = '64-092'
adr1.miasto = 'lublin'

print adr1.ulica
print adr1.__dict__