
'''
def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")
fancy_divide([0, 2, 4], 0)
#error ZeroDivisionError
'''

def fancy_divide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")

fancy_divide([0, 2, 4], 0)
# 0, -2

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try: 
        return item / denom
    except ZeroDivisionError:
        return 0

print(fancy_divide([0, 2, 4], 1))


def fancy_divide(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide( numbers, len(numbers) - 1 )
    except ZeroDivisionError:
        print( "-2" )
    else:
        print( "1" )
    finally:
        print("0:")

fancy_divide([0, 2, 4], 15)

def fancy_divide(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        #except ZeroDivisionError:
            #print("Zero devision")
        #except Exception as ex:
            #print(ex)    
        finally:
            raise Exception("rise exception undefined")
    except Exception as ex:
        print(ex)    
fancy_divide([0, 2, 4], 0)

# defensive programming
# assert statment to raise AssertError
# execution halt, typically check inputs, can be used outputs, locate source of a bug
# assert not ( 0 == 1 ) assert(max_number != 0), "Cannot divide by 0"

def normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers 

try:
      normalize([0, 0, 0])
except ZeroDivisionError:
      print('Invalid maximum element')

List1 = [0, 0, 0]
try:
    assert (max(List1) != 0), "jesus maria"
    normalize(List1)
except ZeroDivisionError:
    print('Invalid maximum element')