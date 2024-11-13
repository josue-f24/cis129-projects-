"""
Created on Wed Nov 13 16:51:58 2024
@author: Josue Monreal
"""

def write_grades_to_file():
    # Open file in write mode
    with open('grades.txt', 'w') as file:
        while True:
            # Prompt the user for input
            grade = input("Enter a grade (or 'done' to stop): ")
            if grade.lower() == 'done':
                break
            try:
                grade = int(grade)  # Convert input to integer
                file.write(f"{grade}\n")  # Write the grade to the file
            except ValueError:
                print("Please enter a valid integer grade or 'done' to stop.")
    print("Grades have been written to grades.txt.")

# Call the function to write grades to the file
write_grades_to_file()


# 9.2 Read grades from a plain text file and calculate average

def read_grades_from_file():
    try:
        with open('grades.txt', 'r') as file:
            grades = []
            total = 0
            count = 0
            # Read each grade from the file
            for line in file:
                try:
                    grade = int(line.strip())  # Remove any extra whitespace
                    grades.append(grade)
                    total += grade
                    count += 1
                except ValueError:
                    print(f"Skipping invalid grade: {line.strip()}")
            
            if count == 0:
                print("No grades found.")
                return

            # Calculate the average
            average = total / count
            print("Grades:", grades)
            print("Total:", total)
            print("Count:", count)
            print("Average:", average)
    
    except FileNotFoundError:
        print("grades.txt file not found.")

# Call the function to read grades and calculate the average
read_grades_from_file()


import csv

# 9.3 Write student records to a CSV file

def write_student_records_to_csv():
    with open('grades.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['firstname', 'lastname', 'exam1grade', 'exam2grade', 'exam3grade'])
        
        while True:
            # Input student information
            first_name = input("Enter student's first name (or 'done' to stop): ")
            if first_name.lower() == 'done':
                break
            last_name = input("Enter student's last name: ")
            try:
                exam1 = int(input("Enter grade for exam 1: "))
                exam2 = int(input("Enter grade for exam 2: "))
                exam3 = int(input("Enter grade for exam 3: "))
            except ValueError:
                print("Invalid grade input. Please enter valid integers for the exam grades.")
                continue

            # Write the student's record to the CSV file
            writer.writerow([first_name, last_name, exam1, exam2, exam3])
            print(f"Record for {first_name} {last_name} has been written to grades.csv.")
    
    print("All student records have been written to grades.csv.")

# Call the function to write student records to CSV
write_student_records_to_csv()

