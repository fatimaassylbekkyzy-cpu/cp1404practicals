for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. count in 10s from 0 to 100:
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. count down from 20 to 1:
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. Ask the user for a number, then print that many stars (*), all on one line.
number_of_stars = int(input("Enter a number: "))
for i in range(number_of_stars):
    print('*', end='')
print()

# d. print lines of increasing stars.
number_of_stars = int(input("Enter a number: "))
for i in range(1, number_of_stars + 1):
    print('*' * i)
print()