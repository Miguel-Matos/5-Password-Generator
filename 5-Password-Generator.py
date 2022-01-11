#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = ""

# for letter in range(nr_letters):
#     r_let = random.randint(0,51)
#     letter = letters[r_let]
#     password += letter


# for symbol in range(nr_symbols):
#     r_let = random.randint(0,8)
#     symbol = symbols[r_let]

#     password += symbol

# for number in range(nr_numbers):
#     r_let = random.randint(0,9)
#     number = numbers[r_let]

#     password += number

# random.shuffle(password)
# print(password)



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []
shuffled_pass = ""

for letter in range(nr_letters):
    r_let = random.randint(0,51)
    letter = letters[r_let]
    password.append(letter)


for symbol in range(nr_symbols):
    r_let = random.randint(0,8)
    symbol = symbols[r_let]

    password.append(symbol)

for number in range(nr_numbers):
    r_let = random.randint(0,9)
    number = numbers[r_let]

    password.append(number)

random.shuffle(password)

for i in password:
    shuffled_pass += i

print(shuffled_pass)