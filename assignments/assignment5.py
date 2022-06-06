# 1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.
import random

random.seed()

num1 = random.randrange(1)
num2 = random.randrange(1, 10)

print(f'Random number between 0 and 1 - {num1}')
print(f'Random number between 1 and 10) - {num2}')

# 2) Use the datetime library together with the random number to generate a random, unique value.
import datetime

print(f'Using randomly generated values to generate a unique date - {datetime.datetime.now() + datetime.timedelta(days = 1, seconds = num1, milliseconds = num2)}')