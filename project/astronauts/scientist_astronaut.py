from astronauts.base_astronaut import BaseAstronaut


class ScientistAstronaut(BaseAstronaut):
    def __init__(self, id_number, salary):
        super().__init__(id_number, salary, "ScientistAstronaut",  70)

    def train(self):
        self.stamina = min(self.stamina + 3, 100)