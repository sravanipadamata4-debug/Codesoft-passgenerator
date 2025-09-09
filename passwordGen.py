import random
import string

# Prompt user for password length
length = int(input('Enter the length of password: ')) 

# Character sets
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# Combine all character sets
all_chars = lower + upper + num + symbols

# Generate random characters
temp = random.sample(all_chars, length)

# Join into a string
password = "".join(temp)

# Display the password
print(password)