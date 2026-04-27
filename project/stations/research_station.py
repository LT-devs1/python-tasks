

from stations.base_station import BaseStation

class ResearchStation(BaseStation):
    def __init__(self, name):
        super().__init__(name , capacity=5)

    def update_salaries(self, min_value: float):
        for astronaut in self.astronauts:
            if astronaut.salary <= min_value and astronaut.specialization == "ScientistAstronaut":
                astronaut.salary += 5000.0