import pandas as pd

# =========================
# TASK 1: Read CSV File
# =========================
def load_data():
    """
    Reads 'data.csv' and returns a Pandas DataFrame.

    Returns:
        pd.DataFrame
    """
    # TODO: Use pandas to read the CSV file
    pass


# =========================
# TASK 2: Average Marks
# =========================
def average_marks(df):
    """
    Calculates the average marks.

    Args:
        df (pd.DataFrame): Input data

    Returns:
        float: Average marks
    """
    # TODO: Return mean of 'marks' column
    pass


# =========================
# TASK 3: Top Student
# =========================
def top_student(df):
    """
    Finds the student with highest marks.

    Args:
        df (pd.DataFrame): Input data

    Returns:
        str: Name of top student
    """
    # TODO: Find row with highest marks and return name
    pass


# =========================
# TASK 4: Passed Students
# =========================
def passed_students(df):
    """
    Filters students who passed (marks >= 50).

    Args:
        df (pd.DataFrame): Input data

    Returns:
        pd.DataFrame
    """
    # TODO: Return filtered DataFrame
    pass


# =========================
# TASK 5: Add Grade Column
# =========================
def add_grade(df):
    """
    Adds a new column 'grade' based on marks:
        A: >= 75
        B: >= 50
        C: < 50

    Args:
        df (pd.DataFrame): Input data

    Returns:
        pd.DataFrame
    """
    # TODO: Create and add 'grade' column
    pass
