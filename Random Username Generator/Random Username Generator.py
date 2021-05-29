import random
import time

# Random Username generator
Names = ["Tom", "Timmy", "Bob", "Sophia", "Olivia", "Riley", "Emma", "Ava", "Liam", "Noah", "Jackson", "Aiden", "Elijah", "Ahmed", "Atif", "Badr", "Basheer", "Dalil", "Dayyan", "Faiz", "Farhan", "Faysal", "Fida", "Ghani", "Ghazi", "Hamza", "Hassan", "Imad", "Iqbal", "Irfan", "Jamal", "Kafeel", "Aminah", "Aisha", "Asma", "Basimah", "Dariya", "Farhana", "Hana", "Huda", "Iman", "Jameela", "Kareema"]
Answer1 = random.choice(Names)
print("Your name was: " + Answer1)

# Asking a question (Too add a number or not to add a number)
M1 = input("Do you want a number too (y = yes, n = no): ")

# If they want a number:
if M1 == "y":
    random_number = random.randint(1, 9999)
    print(random_number)
    time.sleep(2)
    f = f"Your final username is {Answer1}{random_number}"
    print(f) 

# If they dont want a number:
if M1 == "n":
    print("Your final username is: " + Answer1) 
