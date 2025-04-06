from crewai import Agent, Task, Crew
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

# Créer un agent
researcher = Agent(
    role='Chercheur',
    goal='Rechercher des informations pertinentes sur l\'intelligence artificielle',
    backstory='Expert en recherche et analyse d\'informations sur l\'IA',
    verbose=True,
    allow_delegation=False
)

# Créer une tâche
research_task = Task(
    description='Analyser les dernières avancées en intelligence artificielle et fournir un résumé des développements les plus significatifs.',
    expected_output='Un rapport détaillé sur les dernières avancées en IA avec une chronologie des faits majeurs depuis 2018, incluant les développements majeurs et leur impact potentiel.',
    agent=researcher
)

# Créer un crew
crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=True
)

# Exécuter le crew
result = crew.kickoff()
print("\nRésultat de la recherche :")
print(result) 