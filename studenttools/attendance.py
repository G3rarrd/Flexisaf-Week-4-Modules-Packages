import logging
from logging import Logger

LOGGER: Logger = logging.getLogger(__name__)

class Attendance:
    def __init__(self, total_classes: int, max_attendance_score : int):
        if total_classes < 1:
            raise ValueError("Total classes must be greater than 0")
        
        self.__total_classes: int = total_classes
        self.__current_class : int = 0
        self.__attendance_record: list[bool] = [False] * total_classes
        self.__max_attendance_score : float = max_attendance_score

        LOGGER.info(
            f"Attendance created | "
            f"Total Classes: {total_classes}"
        )

    def attend_class(self, present : bool) -> None:
        if self.__total_classes <= self.__current_class:
            LOGGER.warning("Attendance exceeds total classes")
            return
        
        self.__attendance_record[self.__current_class] = present
        self.__current_class += 1

    @property
    def total_classes(self) -> int:
        return self.__total_classes
    
    @property
    def current_class(self) -> int:
        return self.__current_class
    
    @property
    def attendance_record(self) -> list[bool]:
        return self.__attendance_record.copy()
    
    @property
    def attended_count(self) -> int:
        return sum(self.__attendance_record)
    
    @property
    def score(self) -> float:
        return round((self.attended_count / self.__total_classes) * self.__max_attendance_score, 1)