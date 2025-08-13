from crewai import Task
from tools import yt_tool
from agents import blog_researcher,blog_writer


# Reseach Task
research_task = Task(
    dsecription = (
        "Identify the video {topic}."
        "Get detailed information about the video from the channel"
        
    )
)