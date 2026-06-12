# Python Package Projects

## Overview

This repository contains two Python package projects developed to demonstrate modular programming and the creation of reusable Python modules and packages.

### Projects Included

1. **Student Tools Package**

   * Grade calculation
   * Attendance tracking
   * GPA calculation
   * Student performance summaries

2. **Games Package**

   * Guess the Number
   * Dice Roll
   * Rock Paper Scissors
   * Score tracking and session summaries

---

## Learning Outcomes

The projects were developed to achieve the following learning outcomes:

* Build reusable Python modules and packages.
* Organize code using a modular structure.
* Create maintainable and reusable code components.
* Implement input validation and error handling.
* Using __init__.py files to make python files globally aware in the project directory.

---

## Project Structure

```text
repository/
├── studenttools/
│   ├── __init__.py
│   ├── attendance.py
│   ├── course.py
│   ├── course_enrollment.py
│   ├── grade.py
│   ├── student.py
│   └── summary.py
│
├── games/
│   ├── __init__.py
│   ├── game.py
│   ├── guess_number.py
│   ├── dice_roll.py
│   ├── rps.py
│   ├── game_selection.py
│   └── result_table.py
│
├── games.py
├── student_tools.py
└── README.md
```
## Environment Setup
### Create a Virtual Environment
In the project directory run the following command to create the venv virtual environment
python -m venv venv
venv\Scripts\activate
---

## Student Tools Package

### Description

A mini student management system that provides:

* Grade calculations
* Letter grade determination
* GPA calculation
* Attendance tracking
* Student performance reporting

### How to Run

Run the Student Tools application:

```bash
python student_tools.py
```
Note: The student_tools.py file generates sample results only. A user cannot not create results from the terminal. For a different results, customizations and showcase of different results can be made in the student_tools.py file

---

## Games Package

### Description

A collection of simple console games that allows users to choose and play different games from a menu.

Available games:

* Guess the Number
* Dice Roll
* Rock Paper Scissors

### How to Run

Run the Games application:

```bash
python games.py
```

Follow the on-screen menu to select and play a game.

---

## Requirements

* Python 3.13 or later

### Libraries Used

No external libraries are required.

All projects use only Python's standard library.

---

## Data Files

No CSV, JSON, or other external data files are required.

All data used by the applications is generated or managed within the program.

---
