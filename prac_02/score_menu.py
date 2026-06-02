MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

def main():
    """Main menu loop for getting, grading, and displaying score stars"""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_grade(score)
            print(f"User score {score} is {result}.")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def print_stars(score):
    """Print as many stars as the score"""
    print('*' * int(score))


def get_valid_score():
    """Get a valid score"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score

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