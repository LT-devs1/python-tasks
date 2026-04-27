from astronauts.base_astronaut import BaseAstronaut
from astronauts.engineer_astronaut import EngineerAstronaut
from astronauts.scientist_astronaut import ScientistAstronaut
from stations.base_station import BaseStation
from stations.maintenance_station import MaintenanceStation
from stations.research_station import ResearchStation

ASTRONAUTS = [EngineerAstronaut, ScientistAstronaut]


class SpaceAgency:
    VALID_ASTRONAUTS = ["EngineerAstronaut", "ScientistAstronaut"]
    VALID_STATIONS = ["ResearchStation" ,"MaintenanceStation"]
    ASTRONAUTS = [EngineerAstronaut, ScientistAstronaut]
    STATIONS = [ResearchStation, MaintenanceStation]

    def __init__(self):
        self.astronauts: list[BaseAstronaut] = []
        self.stations: list[BaseStation] = []

    def add_astronaut(self, astronaut_type: str, astronaut_id_number: str, astronaut_salary: float):

        if astronaut_type not in self.VALID_ASTRONAUTS:
            raise ValueError("Invalid astronaut type!")

        if any(a for a in self.astronauts if a.id_number == astronaut_id_number):
            raise ValueError(f"{astronaut_id_number} has been already added!")

        astronaut =  next((a for a in self.ASTRONAUTS if a.__name__ == astronaut_type), None)
        astronaut_adding = astronaut(astronaut_id_number , astronaut_salary)
        self.astronauts.append(astronaut_adding)
        return f"{astronaut_id_number} is successfully hired as {astronaut_type}."

    def add_station(self, station_type: str, station_name: str):
        if station_type not in self.VALID_STATIONS:
            raise ValueError("Invalid station type!")

        if any(s for s in self.stations if s.name == station_name):
            raise ValueError(f"{station_name} has been already added!")

        station = next((s for s in self.STATIONS if s.__name__ == station_type),None)
        station_adding = station(station_name)
        self.stations.append(station_adding)
        return f"{station_name} is successfully added as a {station_type}."

    def assign_astronaut(self, station_name: str, astronaut_type: str):
        station = next((s for s in self.stations if s.name == station_name),None)
        astronaut = next((a for a in self.astronauts if a.__class__.__name__ == astronaut_type),None)

        if station is None:
            raise ValueError(f"Station {station_name} does not exist!")

        if astronaut is None:
            raise ValueError("No available astronauts of the type!")

        if station.capacity <= 0:
            return "This station has no available capacity."

        station.astronauts.append(astronaut)
        self.astronauts.remove(astronaut)
        station.capacity -= 1
        return f"{astronaut.id_number} was assigned to {station_name}."

    def train_astronauts(self, station: BaseStation, sessions_number: int):
        for _ in range(sessions_number):
            for astronaut in station.astronauts:
                astronaut.train()

        total = 0
        for a in station.astronauts:
            total += a.stamina

        return f"{station.name} astronauts have {total} total stamina after {sessions_number} training session/s."

    def retire_astronaut(self, station: BaseStation, astronaut_id_number: str):
        max_stamina = 100
        astronaut = next((a for a in station.astronauts if a.id_number == astronaut_id_number),None)

        if astronaut is None or astronaut.stamina >= max_stamina:
           return "The retirement process was canceled."

        station.astronauts.remove(astronaut)
        station.capacity += 1
        return f"Retired astronaut {astronaut_id_number}."


    def agency_update(self, min_value: float):
        stations_status = []

        for station in self.stations:
            station.update_salaries(min_value)

        astronauts_count = len(self.astronauts)
        stations_total_count = len(self.stations)
        total_available_capacity = sum(s.capacity for s in self.stations)
        sorted_stations = sorted(
            self.stations,
            key=lambda s: (-len(s.astronauts), s.name))

        for station in sorted_stations:
            stations_status.append(station.status())

        result = [
            "*Space Agency Up-to-Date Report*",
            f"Total number of available astronauts: {astronauts_count}",
            f"**Stations count: {stations_total_count}; Total available capacity: {total_available_capacity}**"
        ]
        result.extend(stations_status)

        return "\n".join(result)






