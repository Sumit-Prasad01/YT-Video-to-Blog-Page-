from crewai import Agent
from tools import yt_tool


## Create a senior blog content researcher

blog_researcher = Agent(
    role = 'Blog Researcher from Youtube Videos.',
    goal = 'get the relevant video content for the topic {topic} from Yt channel.',
    verbose = True,
    memory = True,
    backstory = (
        "Expert in understanding videos in AI, Data Science, Machine Learning and GenAI and providing suggestion."
    ),
    tools = [yt_tool],
    allow_delegation = True
)

## Creater a Senior Blog Writer Agent with Yt tool.

blog_writer = Agent(
    role = 'Blog Writer',
    goal = 'Narrate compelling tech stories about the video{topic} from Yt channel',
    verbose = True,
    memory = True,
    backstory = (
        "With a flair for simplifying complex topic, you craft" 
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner"
    ),
    tools = [yt_tool],
    allow_delegation = True
)

