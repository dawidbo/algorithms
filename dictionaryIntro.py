
# Dictionary [(custom index)key, value ] but list[ index int, value]
# keys - immutable(int, bool,float, string, tuple), unique 

#initialize
my_Dict = {}
grades = { "davis": "A", "luis": "B","asd":"D"}

# add entries
grades["davisx"] = "C"
print(grades)

# key is in dictionary
print("davis" in grades)

# del() entries in dectionary
del(grades["luis"])
print(grades)

# get all keys like tuple
print(grades.keys())

#get all values like tuple 
print(grades.values())

#example
def how_many(aDict):
    return len(aDict.values())
    
List = {1:"a",2:"a",3:"a",4:"a",5:"a",6:"a"}
print(how_many(List))

animals = { 'a': ['aardvarkf'], 'b': ['baboon'], 'c': ['coati'] }
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print(animals)
# {'a': ['aardvarkf'], 'b': ['baboon'], 'd': ['donkey', 'dog', 'dingo'], 'c': ['coati']}

def findKey( aDict ):
    maxElt = 0
    key = None
    for k in aDict.keys():
        if maxElt < len(aDict[k]):
            maxElt = len(aDict[k])
            key = k
    return key
print( findKey( animals ) ) 
# d