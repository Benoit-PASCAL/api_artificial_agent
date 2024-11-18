# import os

# from dotenv import loads_dotenv
from crewai import Crew
from fastapi import FastAPI
from pydantic import BaseModel

from models.agent import myAgent
from models.task import Task


class BaseAgent(BaseModel):
    name: str
    goal: str
    backstory: str


class BaseTask(BaseModel):
    description: str


class Request(BaseModel):
    agent: BaseAgent
    task: BaseTask


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Je s'appelle Root"}


@app.get("/hello")
async def hello():
    return {"message": "Hello World"}


@app.post("/req")
async def req(request: Request):
    # loads_dotenv()
    # api = os.getenv("OPENAI_API_KEY")

    tmpAgent = myAgent().buildFromJson(request.agent)

    tmpTask = Task().buildFromJson(request.task)

    crew = Crew(
        agents=[tmpAgent],
        tasks=[tmpTask],
        verbose=True
    )

    # result = crew.kickoff()
    result = 'email_management'

    return result
