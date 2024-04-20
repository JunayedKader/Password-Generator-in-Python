import random
required_number  = int(input(f"How many numbers do you required \n"))
required_letter  = int(input(f"How many letter do you required \n"))
required_char  = int(input(f"How many Special characters do you required \n"))

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
spe_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ';', ':', "'", '"', '<', '>', ',', '.', '/', '?']

password_list = []

for n in range(required_letter):
    password_list += random.choice(letters)

for n in range(required_number):
    password_list += str(random.choice(numbers))

for n in range(required_char):
    password_list += random.choice(spe_char)

print(password_list)

random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your Password is : {password}")