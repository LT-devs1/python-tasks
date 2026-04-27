from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish

valid_divers = {"FreeDiver":FreeDiver, "ScubaDiver":ScubaDiver}
valid_fishes = {"PredatoryFish":PredatoryFish, "DeepSeaFish":DeepSeaFish}

class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers:list[BaseDiver] = []
        self.fish_list:list[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):

        diver = next((d for d in self.divers if d.name == diver_name),None)

        if diver_type not in valid_divers:
            return f"{diver_type} is not allowed in our competition."

        if diver:
            return f"{diver_name} is already a participant."

        new_diver = valid_divers[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):

        fish = next((f for f in self.fish_list if f.name == fish_name),None)

        if fish_type not in valid_fishes:
            return f"{fish_type} is forbidden for chasing in our competition."

        if fish:
            return f"{fish_name} is already permitted."

        new_fish = valid_fishes[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):

        diver = next((d for d in self.divers if d.name == diver_name),None)
        fish = next((f for f in self.fish_list if f.name == fish_name),None)

        if diver is None:
            return f"{diver_name} is not registered for the competition."

        if fish is None:
            return f"The {fish_name} is not allowed to be caught in this competition."



        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.has_health_issue = True
            return f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
            if diver.oxygen_level == 0:
                diver.has_health_issue = True
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."

            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):

        divers_to_recover = [d for d in self.divers if d.has_health_issue]
        for diver in divers_to_recover:
            diver.has_health_issue = False
            diver.renew_oxy()

        return f"Divers recovered: {len(divers_to_recover)}"

    def diver_catch_report(self, diver_name: str):

        diver = next((d for d in self.divers if d.name == diver_name),None)
        if diver is None:
            return ""

        result = f"**{diver_name} Catch Report**\n"

        for fish in diver.catch:
            result += fish.fish_details() + "\n"

        return result.strip()

    def competition_statistics(self):
        healthy_divers = [
            d for d in self.divers if not d.has_health_issue
        ]

        sorted_divers = sorted(
            healthy_divers,
            key=lambda d: (-d.competition_points, -len(d.catch), d.name)
        )

        result = "**Nautical Catch Challenge Statistics**\n"

        for diver in sorted_divers:
            result += str(diver) + "\n"

        return result.strip()


