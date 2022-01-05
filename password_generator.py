import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
random.shuffle(letters)
numbers = list("0123456789")
random.shuffle(numbers)
characters = list("~!@#$%^&*()")
random.shuffle(characters)
print("Welcome to the password generator!")
letters_select = int(input(f"How many letters you want your password to have?(from 1 to {len(letters)}): "))
if letters_select > len(letters):
    print("It must be a number between 1 and {}".format(len(letters)))
numbers_select = int(input(f"How many numbers you want your password to have?(from 1 to {len(numbers)}): "))
if numbers_select > len(numbers):
    print("It must be a number between 1 and {}".format(len(numbers)))
characters_select = int(input(f"How many characters you want your password to have?(from 1 to {len(characters)}): "))
if characters_select > len(numbers):
    print("It must be a number between 1 and {}".format(len(characters)))
password_list = []
for char in range(1, letters_select + 1):
    password_list.append(random.choice(letters))
for char in range(1, numbers_select + 1):
    password_list.append(random.choice(numbers))
for char in range(1, characters_select + 1):
    password_list.append(random.choice(characters))
random.shuffle(password_list)
password = ""
for p in password_list:
    password += p

print(f"Password generated is: {password}")
