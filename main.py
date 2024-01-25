import os
from crewai import Crew
from langchain.tools import DuckDuckGoSearchRun
from baby_expert_agents import BabyExpertAgents
from baby_expert_tasks import BabyExpertTasks
from textwrap import dedent

search_tool = DuckDuckGoSearchRun()

class BabyExpertCrew():
    def __init__(self, user_input):
        self.user_input = user_input

    def run(self):
        agents = BabyExpertAgents()
        pediatrician = agents.pediatrician()
        obstetrician = agents.obstetrician()
        child_life_specialist = agents.child_life_specialist()
        development_specialist = agents.development_specialist([search_tool])
        specialist_secretery = agents.secretary()

        tasks = BabyExpertTasks()
        analyze_baby_health_task = tasks.analyze_baby_health(self.user_input, pediatrician)
        prenatal_and_postnatal_care = tasks.prenatal_and_postnatal_care(self.user_input, obstetrician)
        suggest_comforting_activities_task = tasks.suggest_comforting_activities(self.user_input, child_life_specialist)
        recommend_developmental_activities_task = tasks.recommend_developmental_activities(self.user_input, development_specialist)
        summarize_task = tasks.compile_final_guidance(self.user_input, specialist_secretery)

        crew = Crew(
        agents=[pediatrician, obstetrician, child_life_specialist, development_specialist],
        tasks=[analyze_baby_health_task, prenatal_and_postnatal_care, suggest_comforting_activities_task, recommend_developmental_activities_task, summarize_task],
        verbose=True, # You can set it to 1 or 2 to different logging levels
        )
    
        result = crew.kickoff()
        return result

if __name__ == "__main__":
  print("## Welcome to Baby Expert Crew")
  print('-------------------------------')
  user_input = input(
    dedent("""
      What do you want to know?
    """))
  
  baby_expert_crew = BabyExpertCrew(user_input=user_input)
  result = baby_expert_crew.run()
  print("\n\n########################")
  print("## Here is the Report")
  print("########################\n")
  print(result)