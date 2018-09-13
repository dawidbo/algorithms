# method is called when an object is created __init__, self refer to a particular distance
class Coordinate(object):
    def __init__ (self,x,y):
        self.x = x
        self.y = y
    def getX(self): 
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x
    def getY(self):
        return self.y
    def distance(self,other):
        x_def_sq = (self.x - other.x) ** 2
        y_def_sq = (self.y - other.y) ** 2
        return (x_def_sq + y_def_sq)**0.5
    # when call a function by name __str__ call instead memory adress
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def __repr__(self):
        return "Coordinate: "+"("+ self.x +","+ self.y +")"
    def __sub__(self,other):
        return Coordinate( self.x - other.x, self.y - other.y)
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
# c - frame, object on which to call method, distance - name of method
c = Coordinate(3,4)
print(c)
origin = Coordinate(0,0)

print(c.distance(origin))
print(Coordinate.distance(c,origin))

print(type(c)) # <class '__main__.Coordinate'>
print(isinstance(c,Coordinate)) # true
print(repr(c))

a = Coordinate(5,5)
b = Coordinate(4,4)
print(a-b) # <1,1>

print(a==b) # false
print(a.__eq__(b)) # false