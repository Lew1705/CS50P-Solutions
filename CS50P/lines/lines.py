import sys

def main():
    # validate number of command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    # must end with .py
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(filename) as file:
            count = 0

            for line in file:
                stripped = line.strip()

                if stripped == "":
                    continue

                if stripped.lstrip().startswith("#"):
                    continue

                count += 1

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(count)


if __name__ == "__main__":
    main()
