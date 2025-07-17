# Modules

# 1. Built in modullar
# 2. Local təyin etdiyimiz modullar
# 3. Third party modullar (pip vasitəsilə quraşdırılır)

# built in modullara nümunə
# math, random, datetime, json

import math
# from math import sqrt, cos, atan
import random
# import random as ra
# ra.choice


num = math.sqrt(25)

print(num)


numbers = [1, 2, 3, 4, 5, 6]
random_element = random.choice(numbers)
random_elements = random.choices(numbers, k=5)

print(random_element)
print(random_elements)


# 2. Local təyin etdiyimiz modullar
import local_module

print(local_module.get_max_value(numbers))
print(local_module.default_numbers)


# 3. Third party modullar (pip vasitəsilə quraşdırılır)
# pip install Django
# pip install requests
# pip install pandas
