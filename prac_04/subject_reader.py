"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    subject_data = load_subjects(FILENAME)
    display_subjects(subject_data)


def display_subjects(subject_data):
    """Display subject data a different way."""
    for parts in subject_data:
        subject_code = parts[0]
        lecturer = parts[1]
        number_of_students = parts[2]
        print(f"{subject_code} is taught by {lecturer:12} and has {number_of_students:3} students")


def load_subjects(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject = []
    with open(filename) as input_file:
        for line in input_file:
            # print(line)  # See what a line looks like
            # print(repr(line))  # See what a line really looks like
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            parts[2] = int(parts[2])
            # print(parts)  # See what the parts look like (notice the integer is a string)
            # data = [parts[0], parts[1], int(parts[2])]
            # print(data)  # See if that worked
            subject.append(parts)
    return subject


main()