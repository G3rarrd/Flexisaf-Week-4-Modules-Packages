import logging
from logging import Logger

from studenttools.course import Course
from studenttools.attendance import Attendance
from studenttools.grade import letter_grade, grade_point

LOGGER: Logger = logging.getLogger(__name__)

class CourseEnrollment:
    MAX_TEST_SCORE : int = 25
    MAX_EXAM_SCORE : int = 60
    MAX_ASSIGNMENT_SCORE : int = 10
    MAX_ATTENDANCE_SCORE : int = 5

    def __init__(self, student_matric_no : str, course : Course, class_count : int):
        if class_count < 1:
            raise ValueError("Class count must be greater than 0")
        
        self.__course : Course = course
        self.__student_matric_no : str = student_matric_no
        self.__class_count : int = class_count
        self.__attendance : Attendance = Attendance(class_count, self.MAX_ATTENDANCE_SCORE)

        self.__assignment : float = 0.0
        self.__test : float = 0.0
        self.__exam : float = 0.0

        LOGGER.info(
            f"Enrollment made | "
            f"Student: {student_matric_no} | "
            f"Course: {course.code}"
        )

    @property
    def course(self) -> Course:
        return self.__course
    
    @property
    def class_count(self) -> int:
        return self.__class_count

    @property
    def student_matric_no(self) -> str:
        return self.__student_matric_no
    
    # Assignment
    @property
    def assignment(self) -> float:
        return self.__assignment
    
    @assignment.setter
    def assignment(self, score: float) -> None:
        if self.__score_is_invalid(score, float(self.MAX_ASSIGNMENT_SCORE)):
            raise ValueError(f"Assignment score must be between 0 and {self.MAX_ASSIGNMENT_SCORE}")
        self.__assignment = score
    
    # Test
    @property
    def test(self) -> float:
        return self.__test
    
    @test.setter
    def test(self, score: float) -> None:
        if self.__score_is_invalid(score, float(self.MAX_TEST_SCORE)):
            raise ValueError(f"Test score must be between 0 and {self.MAX_TEST_SCORE}")

        self.__test = score
    
    # Exam
    @property
    def exam(self) -> float:
        return self.__exam
    
    @exam.setter
    def exam(self, score: float) -> None:

        if self.__score_is_invalid(score, float(self.MAX_EXAM_SCORE)):
            raise ValueError(
                f"Exam score must be between 0 and {self.MAX_EXAM_SCORE}"
            )
        
        self.__exam = score

    @property
    def attendance(self) -> Attendance:
        return self.__attendance
    
    # Compute result
    @property
    def total(self) -> float:
        return self.__assignment + self.__test + self.__exam + self.__attendance.score
    
    @property
    def weighted_points(self) -> float:
        return self.grade_point * self.__course.unit
    
    @property
    def grade_point(self) -> float:
        return grade_point(self.total)
    
    @property
    def letter_grade(self)-> str:
        return letter_grade(self.total)
    
    def __score_is_invalid(self, score: float, max_score: float) -> bool:
        return score < 0.0 or score > max_score
    
    def __str__(self):
        return (
            f"{self.__student_matric_no} | "
            f"{self.__course.code} | "
            f"Total: {self.total} | "
            f"Grade Point: {self.grade_point}"
        )