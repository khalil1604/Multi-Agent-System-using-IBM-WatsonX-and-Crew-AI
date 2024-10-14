from crewai import Crew, Task, Agent
from crewai_tools import SerperDevTool
from langchain_ibm import WatsonxLLM
import os

os.environ["WATSONX_API_KEY"] = os.getenv["WATSONX_API_KEY"]
os.environ["SERPER_API_KEY"] = os.getenv["SERPER_API_KEY"]
PROJECT_ID = os.getenv["PROJECT_ID"]


# Parameters
parameters = {"decoding_method": "greedy", "max_new_tokens": 500}

# Create the first LLM
llm = WatsonxLLM(
    #model_id="meta-llama/llama-3-70b-instruct",
    model_id = "mistralai/mixtral-8x7b-instruct-v01",
    url="https://eu-de.ml.cloud.ibm.com",
    params=parameters,
    project_id= PROJECT_ID,
)


# Create the function calling llm
function_calling_llm = WatsonxLLM(
    model_id="meta-llama/llama-3-1-70b-instruct",
    url="https://eu-de.ml.cloud.ibm.com",
    params=parameters,
    project_id=PROJECT_ID,
)

# Tools
search = SerperDevTool()

# Create the agent
researcher = Agent(
    llm=llm,
    function_calling_llm=function_calling_llm,
    role="Senior AI Researcher",
    goal="Find promising research in the field of quantum computing.",
    backstory="You are a veteran quantum computing researcher with a background in modern physics.",
    allow_delegation=False,
    tools=[search],
    verbose=1,
)

# Create a task
task1 = Task(
    description="Search the internet and find 5 examples of promising AI research.",
    expected_output="A  bullet point summary on each of the topics. Each bullet point should cover briefly the topic and why the innovation is useful.",
    output_file="task1output.txt",
    agent=researcher,
)

# Create the second agent
writer = Agent(
    llm=llm,
    role="Senior Speech Writer",
    goal="Write engaging and witty keynote speeches from provided research.",
    backstory="You are a veteran quantum computing writer with a background in modern physics.",
    allow_delegation=False,
    verbose=1,
)

# Create a task
task2 = Task(
    description="Write an engaging keynote speech on quantum computing.",
    expected_output="A detailed keynote speech with an intro, body and conclusion.",
    output_file="task2output.txt",
    agent=writer,
)

# Put all together with the crew
crew = Crew(agents=[researcher, writer], tasks=[task1, task2], verbose=1)
print(crew.kickoff())
