from crewai import Agent
from tools import web_tool

from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPEN_API_KEY"] = os.getenv("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")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"


## Create a senior blog content researcher

movie_analyst=Agent(
    role='Movie reviewer from IMDb',
    goal='get the relevant info for the show or movie {topic} from the provided website',
    verboe=True,
    memory=True,
    backstory=(
       "Expert in understanding the movie,its hidden subplots,its human touch and rating it properly" 
    ),
    tools=[web_tool],
    allow_delegation=True

)
