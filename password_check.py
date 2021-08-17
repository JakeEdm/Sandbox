
password_requirements = "**********"

password = input("Enter new password: ")

while len(password) < len(password_requirements):
    print("Invalid password length")
    password = input("Enter new password: ")

for char in password:
    print("*", end="")

