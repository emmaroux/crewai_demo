from crewai import Agent, Task, Crew
from langchain.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Créer un outil de recherche
search_tool = DuckDuckGoSearchRun()

# Créer un agent
researcher = Agent(
    role='Chercheur',
    goal='Rechercher des informations pertinentes sur un sujet donné',
    backstory='Expert en recherche et analyse d\'informations',
    tools=[search_tool],
    verbose=True
)

# Créer une tâche
research_task = Task(
    description='Rechercher des informations sur l\'intelligence artificielle en 2024',
    agent=researcher
)

# Créer un crew
crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=2
)

# Exécuter le crew
result = crew.kickoff()
print("\nRésultat de la recherche :")
print(result) 