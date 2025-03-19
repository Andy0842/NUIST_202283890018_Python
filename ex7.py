#List and Print Students' Name
#Auther: Yang Yue
#Using function

# This program manages a list of student names and prints them with their last names
# It also allows adding new names to the list

def studList():
    # Initial list of student names with their last names
    studentNames = [
        {"first_name": "Lisa", "last_name": "Evans"},
        {"first_name": "Liam", "last_name": "Evans"},
        {"first_name": "Leo", "last_name": "Black"},
        {"first_name": "Larry", "last_name": "Sharp"},
        {"first_name": "Linda", "last_name": "Sharp"}
    ]
    return studentNames

def addToList(studentNames):
    # Ask user for a new first name and last name
    new_first = input("Enter the new student's first name: ")
    new_last = input("Enter the new student's last name: ")
    # Add the new student to the list
    studentNames.append({"first_name": new_first, "last_name": new_last})
    return studentNames

def printNames(studentNames):
    # Print each student's full name
    for student in studentNames:
        print(f"{student['first_name']} {student['last_name']}")

# Main program
if __name__ == "__main__":
    # Create and print the initial list
    students = studList()
    print("Original list of students:")
    printNames(students)

    # Add a new student and print the updated list
    print("\nAdding a new student...")
    students = addToList(students)
    print("\nUpdated list of students:")
    printNames(students)
