#!/usr/bin/env python3

""" Module to test lab3.py """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from lab3 import days_in_month

MONTHS_WITH_31 = ["January", "March", "May", "July", "August", "October", "December"]
MONTHS_WITH_30 = ["April", "June", "September", "November"]
MONTHS_WITH_28_or_29 = ["February"]
MONTHS_WITH_31_LOWER = ["january", "march", "may", "july", "august", "october", "december"]
MONTHS_WITH_30_LOWER = ["april", "june", "september", "november"]
MONTHS_WITH_28_or_29_LOWER = ["february"]

def test_months_with_31():
    """
    Test months with 31 days
    """
def test_months_with_30():
    """
    Test months with 30 days
    """
def test_months_with_28_or_29():
    """
    Test months with 28 or 29 days
    """
    for item in MONTHS_WITH_31:
        assert days_in_month(item) == 31

# Write a test function for the months with 30 days
    for item in MONTHS_WITH_30:
        assert days_in_month(item) == 30

# Write a test function for the months with 28 or 29 days
    for item in MONTHS_WITH_28_or_29:
        assert days_in_month(item) == "28 or 29"


# Write a test function for months that are not capitalized properly
# Hint: use the lower() string method
def lower_case_31():
    for item in  MONTHS_WITH_31_LOWER():
        assert days_in_month(item) == 31
def lower_case_30():
    for item in  MONTHS_WITH_30_LOWER():
        assert days_in_month(item) == 30
def lower_case_28_0r_29():
    for item in  MONTHS_WITH_28_or_29_LOWER():
        assert days_in_month(item) == "28 or 29"


# Write a test function for unexpected input
# Hint: use a try/except block to deal with the exception
# Hint: use data types other than strings as input
def unexpected_input():
    try:
        days_in_month("kjhuy")
    except ValueError:
        assert True

    try:
        days_in_month(7)
    except AttributeError:
        assert True

# Write a test function for unexpected input
# Hint: use a try/except block to deal with the exception
# Hint: use data types other than strings as input

