from studenttools.course import Course
from studenttools.course_enrollment import CourseEnrollment
import logging
from logging import Logger

LOGGER : Logger = logging.getLogger(__name__)


class Student:
    def __init__(self, name : str, matric_no : str, level : int):
        self.__name : str = name
        self.__matric_no : str = matric_no
        self.__records: dict[str, CourseEnrollment] = {}
        self.__level : int = level

        LOGGER.info(
            f"Student created | "
            f"Name: {self.__name} | "
            f"Matric No: {self.__matric_no}"
        )

    def register_course(self, course: Course, class_count : int) -> CourseEnrollment:
        if course.code in self.__records:
            LOGGER.warning(f"{self.__matric_no} already enrolled to {course.code}")
            return self.__records[course.code]
        
        enrollment = CourseEnrollment(self.__matric_no, course, class_count)

        self.__records[course.code] = enrollment

        return enrollment

    def drop_course(self, course_code: str) -> None:
        if course_code not in self.__records:
            LOGGER.warning(f"{course_code} not registered for {self.__matric_no}")
            return

        del self.__records[course_code]
        LOGGER.info(f"{self.__matric_no} dropped course: {course_code}")

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def matric_no(self) -> str:
        return self.__matric_no

    @property
    def level(self) -> int:
        return self.__level
    
    @property
    def records(self) -> dict[str, CourseEnrollment]:
        return self.__records.copy() # the copy method prevents direct modification to the original list
    
    @property
    def total_units(self) -> float:
        return sum(record.course.unit for record in self.__records.values())
    
    @property
    def total_weighted_points(self) -> float:
        return sum(record.weighted_points for record in self.__records.values())
    
    @property
    def gpa(self) -> float:
        return round(self.total_weighted_points / (self.total_units + 1e-6), 2)
    
    def __str__(self) -> str:
        return (
            f"{self.name} "
            f"({self.matric_no}) "
            f"| GPA: {self.gpa}"
        )

    def __repr__(self) -> str:
        return self.__str__()