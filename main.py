
import json
import csv
import os

FILE_NAME = "students.json"


# Load student records
def load_students():
    try:
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        return []

    except (json.JSONDecodeError, OSError) as error:
        print("Error reading file:", error)
        return []


# Save student records
def save_students(students):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)
        return True

    except OSError as error:
        print("Error saving file:", error)
        return False


# Add student
def add_student(students):
    student_id = input("Enter Student ID: ")

    if any(s["id"] == student_id for s in students):
        print("Student ID already exists!")
        return

    name = input("Enter Student Name: ")

    try:
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        if age <= 0 or not 0 <= marks <= 100:
            print("Enter a valid age and marks (0-100).")
            return

    except ValueError:
        print("Please enter valid numbers.")
        return

    course = input("Enter Course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)

    if save_students(students):
        print("Student added successfully!")


# View students
def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n----- STUDENT RECORDS -----")

    for student in students:
        print(student)


# Search student
def search_student(students):
    student_id = input("Enter Student ID to search: ")

    result = list(filter(
        lambda s: s["id"] == student_id,
        students
    ))

    if result:
        print("Student found:", result[0])
    else:
        print("Student not found.")


# Update student
def update_student(students):
    student_id = input("Enter Student ID to update: ")

    student = next(
        (s for s in students if s["id"] == student_id),
        None
    )

    if student is None:
        print("Student not found.")
        return

    name = input("Enter new name: ")
    course = input("Enter new course: ")

    student["name"] = name
    student["course"] = course

    if save_students(students):
        print("Student updated successfully!")


# Delete student
def delete_student(students):
    student_id = input("Enter Student ID to delete: ")

    updated_students = [
        s for s in students if s["id"] != student_id
    ]

    if len(updated_students) == len(students):
        print("Student not found.")
        return

    if save_students(updated_students):
        students[:] = updated_students
        print("Student deleted successfully!")


# Export records to CSV
def export_csv(students):
    try:
        with open("students.csv", "w", newline="") as file:
            fields = ["id", "name", "age", "course", "marks"]

            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(students)

        print("CSV file exported successfully!")

    except OSError as error:
        print("CSV export error:", error)


# Main menu
def main():
    students = load_students()

    while True:
        print("\n===== STUDENT RECORD MANAGEMENT =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Export to CSV")
        print("7. Show Students with Marks >= 50")
        print("8. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student(students)

            elif choice == 2:
                view_students(students)

            elif choice == 3:
                search_student(students)

            elif choice == 4:
                update_student(students)

            elif choice == 5:
                delete_student(students)

            elif choice == 6:
                export_csv(students)

            elif choice == 7:
                passed = [
                    s for s in students if s["marks"] >= 50
                ]
                print("Students with marks >= 50:", passed)

            elif choice == 8:
                print("Thank you for using the application!")
                break

            else:
                print("Please enter a choice between 1 and 8.")

        except ValueError:
            print("Invalid input! Enter a number.")

        except Exception as error:
            print("Unexpected error:", error)

        finally:
            print("Operation completed.")


if __name__ == "__main__":
    main()
