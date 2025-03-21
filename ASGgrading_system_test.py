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
    filename = "students_valid.csv"
    with open(filename, "w") as a:
        a.write("Alice,85")
    # setup
    expected = ("Alice"+': '+"B")
    # invoke
    actual = process_students(filename)
    # analyse
    assert expected==actual

def test_calculate_average_grade():
    filename = "students_valid.csv"
    # setup
    expected = "Class Average: B"
    # invoke
    actual = calculate_average_grade(filename)
    # analyze
    assert expected == actual

def test_count_failing_students():
    filename = "students_valid.csv"
    # setup
    expected = "Number of Failing Students: 0"
    # invoke
    actual = count_failing_students(filename);
    # analyze
    assert expected == actual
