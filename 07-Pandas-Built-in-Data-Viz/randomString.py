import string
import random

# initializing size of string
N = 7

# using random.choices()
# generating random strings
res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))

# print result
print("Random Generated String :-> " + str(res))

print('Password Successfully Generated')
