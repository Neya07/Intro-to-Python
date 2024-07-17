#%%
#PROBLEM 1: FOR LOOPS
#1
for i in range(1,11) :
    print (i)

# %%
#2
name_list = ["Olivia", "Emma", "Jack", "William", "Jessica", "Noah"]
for name in name_list:
    print("Hello,", name)
# %%
#3
sum = 0
int_list = [12, 38, 291, 4895, 2, 34, 920]
for num in int_list:
    sum += num
print("The sum of the numbers",int_list,"is ",sum)

# %%
#4
word = "PYTHON"
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word
print(word)
print(reversed_word)

# %%
#5
string = "DISTINCT"
print(string)
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
for char, count in char_count.items():
    print(char,": ",count)

# %%
#6
gradebook = {
    "Olivia": 98,
    "Emma": 84,
    "Jack": 88,
    "William": 58,
    "Jessica": 93,
    "Noah": 47
}

print("Passing Students:")
for student, grade in gradebook.items():
    if num >= 60:
        print(student,":",num)


# %%
#7
n = int(input("Enter an integer: "))  

for multiplier in range(1, 11):
    product = n * multiplier 
    print(f"{n} x {multiplier} = {product}")

# %%
# PROBLEM 2: WHILE LOOPS   
#8
i = 1
while i in range (1,11):
    print(i)
    i += 1

# %%
#9
while True:
    name = input("Please enter a name(type quit to exit): ")
    if name.lower() == "quit":
        break
    else:
        print("Hello, ", name)

# %%
#PROBLEM 3: CONDTIONALS
#10

n = int(input("Enter an integer: "))
if n == 0:
    print(n,"is neither odd nor even.")
elif n%2 == 0:
    print(n,"is an even integer.")
else:
    print(n,"is an odd integer")


# %%
#11
import random

numbers = [random.randint(1, 100) for _ in range(10)]
smallest = numbers[0]
largest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num
    elif num > largest:
        largest = num

print(numbers)
print("Smallest number: ",smallest)
print("Smallest number: ", largest)
# %%
#12

list_of_fruits = {
    "cherry": 5,
    "raspberry": 6,
    "pineapple": 14,
    "peach": 8,
    "orange": 4,
    "blueberry": 7,
    "apple": 9
}
while True:
    fruit = input("Enter a fruit name (enter 'quit' to exit): ")
    
    if fruit.lower() == "quit":
        break
    elif fruit in list_of_fruits:
        price = list_of_fruits[fruit]
        print("The cost of a(n)",fruit,"is",price,"dollars.")
    else:
        print("Sorry, we don't have that fruit.")
# %%