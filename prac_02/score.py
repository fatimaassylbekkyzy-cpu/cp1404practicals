"""
CP1404/CP5632 - Practical
"""

import random

def main():
    """Program to determine score status"""
    score = float(input("Enter score: "))
    status = determine_grade(score)
    print(f"User score {score} is {status}.")


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