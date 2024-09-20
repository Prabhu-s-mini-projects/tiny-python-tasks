from functools import reduce

#1 Capitalize all pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize_names(name:str)-> str:
    return name.capitalize()

print( list(map(capitalize_names, my_pets)))

# replace above function with lamda
print( list(map(lambda letter: letter.capitalize(), my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

my_numbers.sort()

print(list(zip(my_strings,my_numbers)))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def criteria(score:int)->int:
    return score if score > 50 else None

print(list(filter(lambda mark: mark if mark > 50 else None, scores)))

#4 Combine all numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def accumulator(acc:int,item:int)->int:
    return acc + item

print(reduce(accumulator,(my_numbers+ scores)))

numbers = [1,2,3,4,5]

squared_numbers_using_list_comp = [lambda number: number**2 for number in numbers]
squared_numbers_using_map = list(map(lambda number: number**2,numbers))

print(f"numbers:{numbers}")
print(f"squared_numbers_using_list_comp:{squared_numbers_using_list_comp}")
print(f"squared_numbers_using_map:{squared_numbers_using_map}")

# sorting a list contains tuples
a = [(0,2),(4,3),(9,9),(10,-1)]

a.sort(key=lambda x: x[1])

print(f"a.sort(key=lambda x: x[1]) = {a}")

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

duplicate = list(set([value for value in some_list if some_list.count(value)>1]))

print(duplicate)

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  # code here
    def wrapper(*args, **kwargs):
        if args[0].get("valid"):
            result = fn(*args, **kwargs)
        else:
           print("invalid user")
        return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)