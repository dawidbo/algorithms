
#hierarchia class  
import random
# lancuch class nie ma metody to szuka w gore lancucha
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newName=""):
        self.name = newName
    def __str__(self):
        return "Animal: " + str(self.name) + ":" + str(self.age)

class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "Cat: " + str(self.name) + ":" + str(self.age)
class Rabbit(Animal):
    def speak(self):
        print("meep")
    def __str__(self):
        return "Rabbit: " + str(self.name) + ":" + str(self.age)
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)# calling constructor animal
        Animal.set_name(self, name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def diff_age(self, other):
        diff = self.age - other.age
        if self.age > other.age:
            print( self.name, "is", diff, "years older then", other.name)
        else:
            print( self.name, "is", -diff, "years younger then", other.name)
    def __str__(self):
        return "person:" + str(self.name) + ":" + str(self.age)
class Student(Person):
    def __init__(self,name,age,major=None):
        Person.__init__(self,name,age)
        self.major = major
    def change_major(self,major):
        self= major
    def speak(self):
        r = random.random()
        print("r",str(r))
        if r < 0.25:
            print("<0.25")
        elif 0.25 <= r < 0.75:
            print("< 0.25, 0.75 )")
        else:
            print("0.75 >")
    def __str__(self):
        return "student:" + str(self.name) +":"+str(self.age)+":"+str(self.major) 
    
jelly = Cat(1)
print(jelly.get_name())
jelly.set_name("jellyBelly")
jelly.speak() #shadowing no speak in animal
print(jelly) # __str__ from cat
print(Animal.__str__(jelly)) 

blob = Animal(12)
print(blob) # name is None
blob.set_name() # default parameter use "" empty string
print(blob) # name ""

john = Person("john",20)
dave = Person("dave",30)
john.speak()
john.diff_age(dave)
Person.diff_age(john,dave) # to samo co linia wyzej
        
eric = Student("eric",22,"python")
print(eric)