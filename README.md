# 📊 Pandas CSV Assignment

## 🎯 Objective
Learn how to read, manipulate, and process CSV data using Pandas.

---

## 📂 Dataset
You are given a file: `data.csv` containing student records.

Columns:
- name
- age
- marks

---

## 📝 Tasks

Implement the following functions in `assignment.py`:

### ✅ Task 1: Read CSV
Write a function `load_data()` that reads `data.csv` and returns a Pandas DataFrame.

---

### ✅ Task 2: Average Marks
Write a function `average_marks(df)` that returns the average marks.

---

### ✅ Task 3: Top Student
Write a function `top_student(df)` that returns the name of the student with highest marks.

---

### ✅ Task 4: Filter Students
Write a function `passed_students(df)` that returns students with marks >= 50.

---

### ✅ Task 5: Add Grade Column
Write a function `add_grade(df)` that adds a column `grade`:
- marks >= 75 → "A"
- marks >= 50 → "B"
- else → "C"

---

## 🚀 How to Run

```bash
python assignment.py
