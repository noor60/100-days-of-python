import random
import string

alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)
symbols=['#','$','!','@','$','%','^','&','*','(',')','_','+']
numbers=range(0,10)
# print(alphabet_lower)
# print(alphabet_upper)
# print(symbols)
# print(numbers)
alphabet_number=float(input("How many letters would you like in your password? \n"))
symbol_number=int(input("How many symbols would you like?\n"))
numbers_number=int(input("How many numbers would you like?\n"))

password=[]
for i in range(int(alphabet_number/2)):
    char=random.choice(alphabet_lower)
    password.append(char)
for i in range(int(alphabet_number/2)):
    char=random.choice(alphabet_upper)
    password.append(char)

for i in range(symbol_number):
    char=random.choice(symbols)
    password.append(char)

for i in range(numbers_number):
    char=str(random.choice(numbers))
    password.append(char)

password = "".join(password)
print ('Your random password is',password)

