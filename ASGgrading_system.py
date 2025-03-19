"""This python program determines the grades of given students, based on the numerical grade.
In case of any errors reading the grades, the program returns the corresponding error and allows for retry.
The program also recognizes errors in the grade values (if they are not valid)"""

import csv
import re

def calculate_grade(score):
    try:
        score = float(score)  # Typecasts the score value from string into number
    except ValueError:
        return "Error: Non-numeric score" # Returns error if score is not an integer/float
    
    if score < 0 or score > 100:
        return "Error: Invalid score" # Returns error if score is outside valid range
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"


def process_students(filename):
    try:
        with open(filename, 'r') as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                
                name = row[0]
                score = row[1]
                grade = calculate_grade(score)
                if grade != calculate_grade(score):            # if error message is returned, print "error: <error type> for <name of student>"
                    print(grade,' for ',name)
                else:                           # else, print name and grade normally
                    print(name,': ',grade)
    except FileNotFoundError:
        print("Error: File not found")          # throws error if file unavailable
    except ValueError:
        print("Error: Non-numeric score")


def calculate_average_grade(filename):
    """
    Reads a CSV file and calculates the average of valid scores.
    Returns the letter grade for the average score.
    If no valid scores, returns an error message.
    """
    total_score = 0
    count = 0
    try:
        with open(filename, 'r') as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                
                name = row[0]
                score = row[1]       # values for name & score are set to the data in each row
                grade = calculate_grade(score)
                if grade==calculate_grade(score):        # if it is error-free, carry on
                    total_score += int(score)   # add scores with each other
                    count += 1                  # increment count or no. of scores or students
        if count == 0:
            print("Error: No valid student data")
            return
        average = total_score / count           # calculates avg. and passes into grade calculator
        class_avg = calculate_grade(average)
        print("Class Average: ", class_avg)
    except FileNotFoundError:
        print("Error: File not found")
    except ValueError:
        print("Error: Non-numeric score")


def count_failing_students(filename):
    """
    Counts the number of failing students (score below 60) in the CSV file,
    & returns the count. If file not found, prints error
    """

    failing_count = 0
    failing_regex = "^([0-9]|[1-5][0-9])$"  # to match failing grades (0-59)
    # failing_regex = "[1-5]\d"  # to match failing grades (0-59)


    try:
        with open(filename, 'r') as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                
                name = row[0]
                score = row[1]
                if re.match(failing_regex, str(score)): # check if the score matches the failing pattern
                    failing_count += 1
        print("Number of Failing Students: "+str(failing_count))
    except FileNotFoundError:
        print("Error: File not found")
    except ValueError:
        print("Error: Non-numeric score")

def main():
    while True:
        filename = input("Enter the filename (e.g., students.csv): ")
        try:
            process_students(filename)
            calculate_average_grade(filename)
            count_failing_students(filename)
            break
        except FileNotFoundError:
            retry = input("Do you want to retry with a different filename? (yes/no): ")
            if retry.lower() != 'yes':      # allows user to retry with a different file name in case of fail
              break

if __name__ == "__main__":
    main()
