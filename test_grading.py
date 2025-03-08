import pytest

from grading_system import *

def test_calculate_grade1():
    #setup
    score = -5
    expectedResult = "Error: Invalid score"

    #invoke
    actualResult = calculate_grade(score)

    #analyze
    assert expectedResult == actualResult

def test_calculate_grade2():
    #setup
    score = 90
    expectedResult = "A"

    #invoke
    actualResult = calculate_grade(score)

    #analyze
    assert expectedResult == actualResult

def test_calculate_grade2():
    #setup
    score = 75
    expectedResult = "C"

    #invoke
    actualResult = calculate_grade(score)

    #analyze
    assert expectedResult == actualResult