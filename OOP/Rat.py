# variable class 
class Rat(object):
    tag = 1
    def __init__(self,fname):
        self.name = fname
        self.rid = Rat.tag
        self.lastName = fname.split(" ")[-1]
        Rat.tag += 1

    def get_rid(self):
        return str(self.rid).zfill(3) # 001

    def __str__(self):
        return self.name
    
    """ lt do porownania obiektow """
    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return  self.lastName < other.lastName
        
dave = Rat("dave")
print(dave.get_rid()) # 001


david = Rat("david")
print(david.get_rid()) # 002

eric = Rat("eric")
print(david.get_rid()) # 003

ratList = [eric, dave, david]

for e in ratList:
    print(e)

ratList.sort() # lt do sortowania

for e in ratList:
    print(e)