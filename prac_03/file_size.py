def main():
    """Run the main program loop to ask for filenames and handle missing filenames."""
    filename = input("Filename: ")
    while filename != "":
        try:
            line_count = get_file_line_count(filename)
            print(f"{filename} has {line_count} lines.")
        except FileNotFoundError:
            print(f"ERROR: {filename} does not exist.")

        filename = input("Filename: ")


def get_file_line_count(filename):
    """Get the number of lines in a file."""
    with open(filename, "r") as in_file:
        lines = in_file.readlines()
        return len(lines)


main()