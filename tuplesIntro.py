#switch value
a=1
b=2
temp=a
a=b
b=temp
# tuples immutable and return more on value from a function 
# tuples in the end mark comma to show is tuples
(a,b)=(b,a)
# empty tupels
t=() 
#initailize
t=(1,"one",2)
print(t[1])
#add 
t=(1,"one",2)
t+=(5,6)

print(t[2:3]) # add comma when slice, this is in fact a tuples when last element no comma
print(t[4]) # add no comma 


#retrun more values
def retunMore(p,q):
    p=p+1
    q=q+2
    return (p,q)

(a,b)=retunMore(3,4) 
print(a,b)


def get_Data(aTuples):
    nums=()
    words=()
    for t in aTuples:
        nums += (t[0],)
        if t[1] not in words:
            words+=(t[1],)
    minValue=min(nums)
    maxValue=max(nums)
    uniqueWords=len(words)
    return(minValue, maxValue, uniqueWords) 
        
(small,maximum,countWords)=get_Data(((1,"abc"),(2,"def"),(3,"ghi"), (4,"abc")))
print(small, maximum, countWords)


def oddTuples(aTup):
    words=()
    length=len(aTup) 
    i=0
    for i in range(length):      
        if i%2==0:
            words+=(aTup[i],) 
    return words
def oddTuples1(aTup):
    return aTup[::2]

tupless=oddTuples(('I', 'am', 'a', 'test', 'tuple'))
print(tupless)