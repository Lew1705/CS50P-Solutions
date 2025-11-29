import sys
import csv
from tabulate import tabulate

table = []

def main():
    # validate number of command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(filename) as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))
main()
