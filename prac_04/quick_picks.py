import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def main():
    """Program to ask user for number of quick picks and display formatted results."""
    quick_picks = int(input("How many quick picks? "))
    for i in range(quick_picks):
        quick_pick = generate_quick_pick()
        result = ' '.join([f"{number:2}" for number in quick_pick])
        print(result)


def generate_quick_pick():
    """Generate a single sorted list of unique random numbers based on constants."""
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    return sorted(numbers)


main()
