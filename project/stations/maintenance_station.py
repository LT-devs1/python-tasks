from stations.base_station import BaseStation


class MaintenanceStation(BaseStation):
    def __init__(self, name):
        super().__init__(name , capacity=3)

    def update_salaries(self, min_value: float):
        for astronaut in self.astronauts:
            if astronaut.salary <= min_value and astronaut.specialization == "EngineerAstronaut":
                astronaut.salary += 3000.0