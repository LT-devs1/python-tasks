from astronauts.base_astronaut import BaseAstronaut


class EngineerAstronaut(BaseAstronaut):
    def __init__(self, id_number, salary):
        super().__init__(id_number, salary, "EngineerAstronaut", 80)

    def train(self):
        self.stamina = min(self.stamina + 5, 100)