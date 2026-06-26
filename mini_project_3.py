# -----------------------------------
# ======== PASSWORD GENERATOR =======
# -----------------------------------


import random
import string

length = int(input("Length: "))

chars = string.ascii_letters + string.digits + "@#$%"
password = ""

for i in range(length):
    password += random.choice(chars)

print(password)