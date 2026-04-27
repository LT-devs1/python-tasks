from abc import ABC, abstractmethod
import re

class BaseStation(ABC):
    def __init__(self, name:str, capacity:int):
        self.__name = name
        self.__capacity = capacity
        self.astronauts = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        pattern = r'^[A-Za-z0-9-]+$'
        if not isinstance(value, str) or not re.match(pattern, value):
            raise ValueError("Station names can contain only letters, numbers, and hyphens!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("A station cannot have a negative capacity!")
        self.__capacity = value

    def calculate_total_salaries(self):
        total_salary = 0
        for astronauts in self.astronauts:
            total_salary += astronauts.salary
        return sum(a.salary for a in self.astronauts)

    def status(self):
        if not self.astronauts:
            astronauts_str = "N/A"
            total_salaries = "0.00"
        else:
            astronaut_ids = sorted(a.id_number for a in self.astronauts)
            astronauts_str = " #".join(astronaut_ids)
            total_salaries = f"{self.calculate_total_salaries():.2f}"
        return f"Station name: {self.name}; Astronauts: {astronauts_str}; Total salaries: {total_salaries}"
    @abstractmethod
    def update_salaries(self, min_value: float):
        pass

