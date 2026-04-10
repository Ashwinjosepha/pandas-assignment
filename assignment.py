import pandas as pd

# =========================
# TASK 1: Read CSV File
# =========================
def load_data():
    return pd.read_csv("data.csv")


# =========================
# TASK 2: Average Marks
# =========================
def average_marks(df):
    return df["marks"].mean()


# =========================
# TASK 3: Top Student
# =========================
def top_student(df):
    return df.loc[df["marks"].idxmax(), "name"]


# =========================
# TASK 4: Passed Students
# =========================
def passed_students(df):
    return df[df["marks"] >= 50]


# =========================
# TASK 5: Add Grade Column
# =========================
def add_grade(df):
    def get_grade(marks):
        if marks >= 75:
            return "A"
        elif marks >= 50:
            return "B"
        else:
            return "C"

    df["grade"] = df["marks"].apply(get_grade)
    return df
