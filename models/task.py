from crewai import Task as cTask


class Task:
    def buildFromJson(self, json):
        return cTask(
            description=json["description"],
            expected_output='A paragraph',
            verbose=True,
        )
