from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
import os
from crewai.llms import LiteLLM

# Load environment variables
load_dotenv()

# Ensure OPENAI_API_KEY is set (some internal tools expect it even if not used)
if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = "dummy"

# Initialize the LLM using Groq + LLaMA3
llm = LiteLLM(
    model="llama3-8b-8192",  # Must match the model on your Groq account
    api_key=os.getenv("GROQ_API_KEY"),
    provider="groq"
)

# Create a senior blog content researcher
blog_researcher = Agent(
    role='Blog Researcher from YouTube Videos',
    goal='Get the relevant video content for the topic {topic} from a YouTube channel.',
    verbose=True,
    memory=True,
    backstory=(
        "An expert in understanding videos related to AI, Data Science, Machine Learning, and GenAI. "
        "Provides relevant suggestions based on YouTube content."
    ),
    tools=[yt_tool],
    allow_delegation=True
)

# Create a senior blog writer
blog_writer = Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video topic {topic} from the YouTube channel.',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate. "
        "Your writing makes cutting-edge discoveries accessible to a broader audience."
    ),
    tools=[yt_tool],
    allow_delegation=True
)
