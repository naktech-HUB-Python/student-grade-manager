# Student Grade Manager
# Portfolio Project - Version 2.0

def calculate_average(grades):
    return sum(grades) / len(grades)


def get_performance(average):
    if average >= 50:
        return "Pass"
    return "Fail"


def get_student_count():
    while True:
        try:
            count = int(input("How many students? "))

            if count <= 0:
                print("Please enter a number greater than zero.")
                continue

            return count

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_grade(grade_number):
    while True:
        try:
            grade = float(input(f"Enter grade {grade_number}: "))

            if 0 <= grade <= 100:
                return grade

            print("Grade must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_student_name():
    while True:
        name = input("Enter student name: ").strip()

        if name:
            return name

        print("Student name cannot be empty.")


def main():
    students = []

    print("=" * 35)
    print("       STUDENT GRADE MANAGER")
    print("=" * 35)

    number_of_students = get_student_count()

    for i in range(number_of_students):
        print(f"\nStudent {i + 1}")

        name = get_student_name()

        grades = []

        for j in range(3):
            grade = get_grade(j + 1)
            grades.append(grade)

        average = calculate_average(grades)
        performance = get_performance(average)

        student = {
            "name": name,
            "grades": grades,
            "average": average,
            "performance": performance
        }

        students.append(student)

    print("\n" + "=" * 35)
    print("          STUDENT RESULTS")
    print("=" * 35)

    for student in students:
        print(f"\nName: {student['name']}")
        print(f"Grades: {student['grades']}")
        print(f"Average: {student['average']:.2f}")
        print(f"Result: {student['performance']}")

    highest_student = max(
        students,
        key=lambda student: student["average"]
    )

    print("\n" + "=" * 35)
    print("      TOP PERFORMING STUDENT")
    print("=" * 35)

    print(f"Name: {highest_student['name']}")
    print(f"Average: {highest_student['average']:.2f}")

    passed = sum(
        1 for student in students
        if student["performance"] == "Pass"
    )

    failed = len(students) - passed

    print("\n" + "=" * 35)
    print("          SUMMARY REPORT")
    print("=" * 35)

    print(f"Total students: {len(students)}")
    print(f"Students passed: {passed}")
    print(f"Students failed: {failed}")

    print("\nGrade management completed successfully!")


if __name__ == "__main__":
    main()
