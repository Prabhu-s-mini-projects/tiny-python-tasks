from functools import reduce

from numpy.ma.core import outer


# Using recursive method
def fib_r(n:int)->int:

    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fib_r(n-2) + fib_r(n-1)


# Using generator
def fib_g(n:int):
    n1  = 0
    n2 = 1
    for i in range(n):
        yield n2
        added = n1 + n2
        n1 = n2
        n2 = added



print(fib_r(19))

for i in fib_g(19):
    print(i)

result = ""
for n in range(2000,3200):
    if n % 7 == 0 and n % 5 != 0:
        result += str(n) + ","

print(result)

# using recursive
def fact_r(n:int)-> int:

    if n == 1:
        return 1
    else:
        return n * fact_r(n-1)

def shotfunc(n:int)-> int: return 1 if n==1 else n *shotfunc(n-1)

print(shotfunc(8))
print(fact_r(8))

print({number: number**2 for number in range(1,9)})

print(dict(enumerate(i*i for i in range(9))))

def fun(acc,item):
    print(f"{acc+item = }")
    return acc + item

print(reduce(fun,range(1,8)))

var = "34,67,55,33,12,98"
list_var = var.split(",")
tuple_var = tuple(var.split(","))
print(list_var)
print(tuple_var)
import  math

input_d = "100,150,180"
output = [str(int (math.sqrt(2*50*float(d)/30))) for d in input_d.split(",")]

print(",".join(output))

x = 3
y = 5

two_d_array =[[r*c for c in range(y)] for r in range(x)]
print(two_d_array)

words = "without,hello,bag,world"
output = ",".join(sorted(words.split(",")))
print(output)