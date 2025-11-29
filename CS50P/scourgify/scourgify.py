import sys
import csv

def main():

    # must have exactly two arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # must be csv
    if not input_file.endswith(".csv"):
        sys.exit(f"Could not read {input_file}")

    students = []

    # read input CSV
    try:
        with open(input_file) as before:
            reader = csv.DictReader(before)
            for row in reader:
                last, first = row["name"].split(", ")
                students.append({
                    "first": first,
                    "last": last,
                    "house": row["house"]
                })
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

    # write output CSV
    with open(output_file, "w", newline="") as after: #a dict writer is where every row is a dictionary
        writer = csv.DictWriter(after, fieldnames=["first", "last", "house"]) #this controls the order of the columns
        writer.writeheader()
        for student in students:
            writer.writerow(student)


main()
