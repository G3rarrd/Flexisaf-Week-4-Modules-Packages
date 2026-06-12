from studenttools.course import Course
from studenttools.course_enrollment import CourseEnrollment
from studenttools.student import Student

from studenttools.summary import student_summary

import logging
import random

# Activate Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(name)s | %(message)s"
)


def test_courses() -> list[Course]:
    """ For Testing Purposes """
    courses : list[Course] = []

    courses.append(Course("MTH101", "Mathematics I", 4))
    courses.append(Course("CSC101", "Introduction to Programming", 3))
    courses.append(Course("PHY101", "Physics I", 3))
    courses.append(Course("GST101", "Use of English", 2))
    courses.append(Course("CHM101", "Chemistry I", 3))
    courses.append(Course("BIO101", "Biology I", 2))

    return courses


def test_students() -> list[Student]:
    """For Testing Purposes"""

    students: list[Student] = []

    students.append(Student("Saka Ahmed", "RGU/UG/3092", 100))
    students.append(Student("Amaka Okafor", "RGU/UG/1123", 100))
    students.append(Student("John Musa", "RGU/UG/4410", 100))
    students.append(Student("Fatima Bello", "RGU/UG/2201", 100))
    students.append(Student("David Eze", "RGU/UG/7812", 100))
    students.append(Student("Grace Adeyemi", "RGU/UG/6654", 100))

    return students

def simulate_attendance(record : CourseEnrollment, attendance_probability : float) -> None:
    for _ in range(record.class_count):
        present : bool = random.random() < attendance_probability

        record.attendance.attend_class(present)

def generate_random_course_scores(enroll : CourseEnrollment) -> None:
    # max range is based on the constants at course enrollement
    enroll.assignment = float(random.randint(3, enroll.MAX_ASSIGNMENT_SCORE))
    enroll.test = float(random.randint(5, enroll.MAX_TEST_SCORE))
    enroll.exam = float(random.randint(15, enroll.MAX_EXAM_SCORE))

def simulate_students_enrollments() -> list[Student]:
    """ For testing purposes """
    courses : list[Course] = test_courses()
    students : list[Student] = test_students()

    for student in students:
        for course in courses:
            record : CourseEnrollment = student.register_course(course, random.randint(7, 10))
            generate_random_course_scores(record)
            simulate_attendance(record, 0.9)

    return students

def main():
    enrolled_students : list[Student] = simulate_students_enrollments()

    for student in enrolled_students:
        summary : str = student_summary(student)
        print("\n")

if "__main__" == __name__:
    main()
