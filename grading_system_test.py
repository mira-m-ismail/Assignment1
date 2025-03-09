from ASGgrading_system import *

def test_calculate_grade():
    # setup
    score1 = (-5)
    expect1 = 'Error: Invalid score'
    score2 = 90
    expect2 = 'A'
    score3 = 75
    expect3 = 'C'
    # invoke
    result1 = calculate_grade(score1)
    result2 = calculate_grade(score2)
    result3 = calculate_grade(score3)
    # analyse
    assert result1==expect1
    assert result2==expect2
    assert result3==expect3


# unit tests
def test_process_students_valid():
    filename = "valid.csv"
    with open(filename, "w") as file:
        file.write("Alice,85\nBob,92\nCharlie,76\n")
    process_students(filename)  # Alice: B, Bob: A, Charlie: C

def test_process_students_invalid_file():
    filename = "non_existing.csv"
    process_students(filename)  # Error: File not found

def test_process_students_invalid_data():
    filename = "invalid.csv"
    with open(filename, "w") as file:
        file.write("Alice,abc\nBob,92\nCharlie,76\n")
    process_students(filename)  # Error: Non-numeric score for Alice

def test_calculate_average_grade():
    filename = "valid_avg.csv"
    with open(filename, "w") as file:
        file.write("Alice,85\nBob,92\nCharlie,76\n")
    calculate_average_grade(filename)  # Class Average: B

def test_calculate_average_grade_invalid_file():
    filename = "non_existing_avg.csv"
    calculate_average_grade(filename)  # Error: File not found

def test_count_failing_students():
    filename = "valid_fail_count.csv"
    with open(filename, "w") as file:
        file.write("Alice,85\nBob,92\nCharlie,76\nDavid,45\n")
    count_failing_students(filename)  # Number of Failing Students: 1

def test_count_failing_students_invalid_file():
    filename = "non_existing_fail_count.csv"
    count_failing_students(filename)  #Error: File not found
