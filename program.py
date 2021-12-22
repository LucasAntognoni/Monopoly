import sys


def main():
    """
        Main function.
    """

    # Set default values
    max_number_of_turns = 1000
    number_of_simulations = 300

    # Check for input parameters
    try:
        if len(sys.argv) == 3:
            number_of_simulations = int(sys.argv[1])
            max_number_of_turns = int(sys.argv[2])
    except Exception as e:
        print(f"Error reading input parameters!\nException: {e}.")
        exit(0)

    # Validate parameters
    if number_of_simulations <= 0 or max_number_of_turns < 4:
        print("Invalid input parameters!")
        exit(0)


if __name__ == '__main__':
    main()
