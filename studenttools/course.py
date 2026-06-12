import logging
from logging import Logger

LOGGER : Logger = logging.getLogger(__name__)



class Course:
    def __init__(self, code : str, title : str, unit : float):
        if unit <= 0:
            raise ValueError("Unit must be greater than 0")
        
        if not code.strip():
            raise ValueError("Course code cannot be empty")
        
        if not title.strip():
            raise ValueError("Course title cannot be empty")
        
        self.__code : str = code
        self.__title : str = title
        self.__unit : float = unit

        
        LOGGER.info(f"Course created : {code} | {title} | Unit: {unit} ")



    @property
    def code(self) -> str:
        return self.__code

    @property
    def title(self) -> str:
        return self.__title

    @property
    def unit(self) -> float:
        return self.__unit

    def __str__(self) -> str:
        return (
            f"{self.code} | "
            f"{self.title} | "
            f"Unit: {self.unit} | "
        )