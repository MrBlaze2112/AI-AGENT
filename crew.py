from crewai import Crew,Process
from agents import movie_analyst
from tasks import write_task


# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
  agents=[movie_analyst],
  tasks=[write_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

## start the task execution process with enhanced feedback
result=crew.kickoff(inputs={'topic':'Barbie v/s Oppenheimer'})
print(result)
