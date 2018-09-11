# nested function simple example
def func_a():
    print("A")

def func_b(x):
    print("B")
    return x

def func_c(x):
    print("C")
    return x

print(func_c(func_b(func_a())))
#A,B,C

def a(x):
    print("a")
    return x


def b(x):
    print("b")
    return a(x)

b(2)
#b,a