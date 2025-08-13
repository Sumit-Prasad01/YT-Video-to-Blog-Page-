from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
from crewai.config import LLMConfig
import os

# Load environment variables from .env
load_dotenv()

# Dummy OPENAI key required by some tools
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "dummy")

# Define your custom LLM (Groq with LLaMA3)
llm_config = LLMConfig(
    provider="groq",
    config={
        "model": "llama3-8b-8192",
        "api_key": os.getenv("GROQ_API_KEY"),
    }
)

# Create Blog Researcher Agent
blog_researcher = Agent(
    role="Blog Researcher from YouTube Videos",
    goal="Get relevant video content for topic {topic} from YouTube.",
    backstory=(
        "Expert at analyzing AI, Data Science, and ML videos on YouTube. "
        "You extract key insights and recommend high-quality content."
    ),
    tools=[yt_tool],
    verbose=True,
    memory=True,
    llm_config=llm_config,
    allow_delegation=True,
)

# Create Blog Writer Agent
blog_writer = Agent(
    role="Blog Writer",
    goal="Create engaging blog articles from YouTube content about {topic}.",
    backstory=(
        "A skilled storyteller who turns technical concepts into accessible blog posts. "
        "You make AI and Data Science topics enjoyable for all readers."
    ),
    tools=[yt_tool],
    verbose=True,
    memory=True,
    llm_config=llm_config,
    allow_delegation=True,
)
