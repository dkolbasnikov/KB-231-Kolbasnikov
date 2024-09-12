import csv
import sys

def load_data(file_name):
    students = []
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"Name": row["Name"], "Phone": row["Phone"]})
    return students

def save_data(file_name, students):
    with open(file_name, mode='w', newline='') as file:
        fieldnames = ["Name", "Phone"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)

def main():
    if len(sys.argv) != 2:
        print("Usage: python phonebook.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    students = load_data(input_file)
    

    output_file = "lab2_out.csv"
    save_data(output_file, students)
    print(f"Data saved to {output_file}")

if __name__ == "__main__":
    main()
