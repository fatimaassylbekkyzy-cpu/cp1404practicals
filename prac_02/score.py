"""
CP1404/CP5632 - Practical
"""

import random

def main():
    """Program to determine score status"""
    score = float(input("Enter score: "))
    status = determine_grade(score)
    print(f"User score {score} is {status}.")

    if status == "Excellent":
        print("You get a prize!")

    random_score = random.randint(0, 100)
    random_status = determine_grade(random_score)
    print(f"Random: {random_score} = {random_status}")


def determine_grade(score):
    """Determine the score status based on the score value"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()