class IntSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""
    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self, other):
        """Assumes other is an intSet
           Returns a new intSet containing elements that appear in both sets."""
        # Initialize a new intSet    
        commonValueSet = IntSet()
        # Go through the values in this set
        for val in self.vals:
            # Check if each value is a member of the other set    
            if other.member(val):
                commonValueSet.insert(val)
        return commonValueSet

    def notIntersect(self, other):
        """Assumes other is an intSet
           Returns unique."""
        commonValueSet = IntSet()
        for elt in self.vals:
            commonValueSet.insert(elt)
        for val in other.vals:
            if not self.member(val):
                commonValueSet.insert(val)
            else:
                commonValueSet.remove(val)
        return commonValueSet

    def __len__(self):
        return len(self.vals)

l1 = IntSet()
l1.insert(1)
l1.insert(2)
l1.insert(5)
print(l1)

l2 = IntSet()
l2.insert(3)
l2.insert(4)
l2.insert(5)
print(l2)

print(l1.intersect(l2))
print(l1.notIntersect(l2))