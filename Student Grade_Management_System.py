students = []


def calculate_grade(avg):
    if avg >= 80:
        return "A+"
    elif avg >= 70:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


def add_student():
    name = input("Enter student name: ")

    math = float(input("Enter Math marks: "))
    science = float(input("Enter Science marks: "))
    english = float(input("Enter English marks: "))

    marks = [math, science, english]
    total = sum(marks)
    avg = total / 3
    grade = calculate_grade(avg)

    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "avg": avg,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!\n")



def view_students():
    if not students:
        print("No student records found!\n")
        return

    print("\nStudent Records")
    print("=" * 40)

    for s in students:
        print(f"Name   : {s['name']}")
        print(f"Marks  : {s['marks']}")
        print(f"Total  : {s['total']}")
        print(f"Avg    : {s['avg']:.2f}")
        print(f"Grade  : {s['grade']}")
        print("-" * 40)


def update_student():
    name = input("Enter student name to update: ")

    for s in students:
        if s["name"].lower() == name.lower():

            math = float(input("Enter new Math marks: "))
            science = float(input("Enter new Science marks: "))
            english = float(input("Enter new English marks: "))

            marks = [math, science, english]
            s["marks"] = marks
            s["total"] = sum(marks)
            s["avg"] = s["total"] / 3
            s["grade"] = calculate_grade(s["avg"])

            print("Student updated successfully!\n")
            return

    print("Student not found!\n")



def delete_student():
    name = input("Enter student name to delete: ")

    for s in students:
        if s["name"].lower() == name.lower():
            students.remove(s)
            print("Student deleted successfully!\n")
            return

    print("Student not found!\n")



def main():
    while True:
        print("Student Grade Management System : ")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting system... Goodbye!")
            break
        else:
            print("Ivalid choice! Try again.")



if __name__ == "__main__":
    main()