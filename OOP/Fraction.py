class Fraction(object):
    def __init__(self,numer,denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer) + " / " + str(self.denom)
    def getNumber(self):
        return self.numer
    def getDenom(self):
        return self.denom
    def __add__(self,other):
        numerNew = other.getDenom() * self.getNumber() + other.getNumber() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return Fraction(numerNew, denomNew)
    def __sub__(self,other):
        numerNew = other.getDenom() * self.getNumber() - other.getNumber() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return Fraction(numerNew, denomNew)
    def convert(self):
        return self.getNumber() / self.getDenom()

#objFrac = Fraction(1,2)
#print(objFrac)
#print(objFrac.getNumber())
#print(objFrac.getDenom())

oneHalf = Fraction(1,2)
twoThirds = Fraction(2,3)

new = oneHalf + twoThirds
print(new)
new = oneHalf - twoThirds
print(new)
print(new.convert())