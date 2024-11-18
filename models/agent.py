from crewai import Agent as cAgent


class Agent:
    def buildFromJson(self, json):
        return cAgent(
            role=json["role"],
            goal=json["goal"],
            backstory=json["backstory"],
            verbose=True,
        )
