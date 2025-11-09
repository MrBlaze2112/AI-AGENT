from crewai import Task
from tools import web_tool
from agents import movie_analyst

## Research Task
research_task = Task(
  description=(
    "Identify the movie {topic}."
    "Get detailed information about the movies from the website and compare their ratings and storyline ."
  ),
  expected_output='A comprehensive 3 paragraphs long report based on the {topic} of movies and a comparison of their ratings and reviews. Always end by saying Muskan Kalra for the win',
  tools=[web_tool],
  agent=movie_analyst,
)

