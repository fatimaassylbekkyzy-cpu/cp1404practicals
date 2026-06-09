import random

print(random.randint(5, 20))  # line 1
# I got: 10, 18, 15.
# Smallest: 5; Largest: 20.

print(random.randrange(3, 10, 2))  # line 2
# I got: 5, 3, 9.
# Smallest: 3; Largest: 9.
# Cannot get 4 because the step size is 2, starting from 3, which means it can only pick odd numbers.

print(random.uniform(2.5, 5.5))  # line 3
# I got: 4.055162666600102
# Smallest: 2.5; Largest: 5.5

print(random.randint(1, 100))