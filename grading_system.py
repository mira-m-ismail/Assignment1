import os

def calculate_grade(score):

    try:
        score = float(score)
    except ValueError:
        return 'Error: Non-numeric score'

    if score<0 or score>100:
        return 'Error: Invalid score'
    if score>= 90:
        return 'A'
    elif score>=80:
        return 'B' 
    elif score>=70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def process_students(filename):

    if not os.path.exists(filename):
        print('Error:File not found')
        return
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) != 2:
                    print('Error:Incorrect data format in line:', line)
                    continue
                name, score_str = parts
                grade = calculate_grade(score_str)
                print(name.strip() + ': ' + grade)
    except Exception as e:
        print('An error occurred while processing the file:', e)

def calculate_average_grade(filename):
    """
    Reads a CSV file and calculates the average of valid scores.
    Returns the letter grade for the average score.
    If no valid scores, returns an error message.
    """
    if not os.path.exists(filename):
        return 'Error: File not found'
    total = 0.0
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) != 2:
                continue
            _, score_str = parts
            try:
                score = float(score_str)
            except ValueError:
                continue  
            if 0 <= score <= 100:
                total += score
                count += 1
    if count == 0:
        return 'Error: No valid scores found'
    average = total / count
    return calculate_grade(average)

def count_failing_students(filename):
    """
    Counts the number of failing students (score below 60) in the given CSV file.
    Returns the count. If file not found, prints error and returns None.
    """
    if not os.path.exists(filename):
        print('Error: File not found')
        return None
    count_failing = 0
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) != 2:
                continue
            _, score_str = parts
            try:
                score = float(score_str)
            except ValueError:
                continue
            if 0 <= score < 60:
                count_failing += 1
    return count_failing
