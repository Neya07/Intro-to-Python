#%%
#1
name = "Neya Sathiya"
print(name)

#%%
#2
age = 15
print(age)

# %%
#3
height = 1.47
print(height)

# %%
#4
age = 15

height = 1.47

add = age + height
print(add)

multiply = age*height
print(multiply)

divide = height//age
print(divide)

# %%
#5
intro = "Neya 15"
print(intro.split())

# %%
#6
intro = "Neya 15"
print(intro.upper())
print(intro.lower())
print(intro.title())
print(intro.swapcase())

# %%
#7
hobbies = ["Dancing", "Researching", "Crafting"]
print(hobbies)

# %%
#8
hobbies = ["Dancing", "Researching", "Crafting"]
hobbies.append("Sleeping")
print(hobbies)
hobbies.remove("Dancing")
print(hobbies)
hobbies.reverse()
print(hobbies)
hobbies = ["Crafting", "Researching", "Sleeping"]
print(hobbies)

# %%
#9
name = "Neya Sathiya"
age = 15
height = 1.47
hobbies = ["Dancing", "Researching", "Crafting"]

profile = {

    "Name": name,
    "Age": age,
    "Height": height,
    "Hobbies": hobbies
    }

print(profile)
# %%
#10
name = "Neya Sathiya"
age = 15
height = 1.47
hobbies = ["Dancing", "Researching", "Crafting"]

profile = {

    "Name": name,
    "Age": age,
    "Height": height,
    "Hobbies": hobbies
    }

profile["Favorite Color"] = "Pink"
print(profile)

del profile["Height"]
print(profile)

print(hobbies)

profile["Age"] = age + 1
print(profile)
