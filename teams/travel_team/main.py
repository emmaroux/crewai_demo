from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

def run_travel_team():
    # Créer les agents
    guide_local = Agent(
        role='Guide Local Expert',
        goal='Fournir des informations détaillées et authentiques sur la ville, sa culture et ses environs',
        backstory="""Vous êtes un guide local expert avec une connaissance approfondie de la ville 
        et de sa culture. Vous connaissez les meilleurs endroits cachés, les expériences authentiques 
        et les aspects pratiques de la vie locale. Vous avez une expertise particulière sur les excursions 
        dans le désert et les activités traditionnelles comme les balades à dos de dromadaire. Vous pouvez 
        donner des conseils sur la sécurité, la santé, et les coutumes locales.""",
        verbose=True,
        allow_delegation=False
    )

    expert_tech = Agent(
        role='Expert Écosystème Tech',
        goal='Identifier et analyser l\'écosystème technologique local',
        backstory="""Vous êtes un expert en écosystèmes technologiques avec une attention particulière 
        portée à l'IA et aux enjeux de souveraineté technologique. Vous connaissez les acteurs clés, 
        les startups innovantes et les initiatives liées aux communs numériques. Vous avez un réseau 
        étendu dans le domaine tech.""",
        verbose=True,
        allow_delegation=False
    )

    expert_voyage = Agent(
        role='Expert Voyage et Santé',
        goal='Créer un itinéraire de voyage complet et pratique avec conseils sanitaires',
        backstory="""Vous êtes un expert en organisation de voyages avec une expertise particulière 
        dans la planification de déplacements professionnels et culturels. Vous connaissez les meilleures 
        options de transport, d'hébergement et pouvez créer des itinéraires optimisés. Vous avez également 
        une expertise en médecine du voyage et conseils sanitaires pour les destinations internationales.""",
        verbose=True,
        allow_delegation=False
    )

    coordinateur = Agent(
        role='Coordinateur de Voyage',
        goal='Créer un itinéraire de voyage optimal en combinant les informations culturelles, tech et pratiques',
        backstory="""Vous êtes un expert en création d'expériences de voyage uniques qui combine 
        parfaitement découverte culturelle, rencontres professionnelles et aspects pratiques. 
        Vous savez créer des itinéraires équilibrés qui permettent de vivre des expériences authentiques 
        tout en respectant les contraintes logistiques.""",
        verbose=True,
        allow_delegation=False
    )

    # Créer les tâches
    tache_guide = Task(
        description="""Analysez la ville d'Essaouira au Maroc et ses environs en tant que guide local. 
        Fournissez des informations précises sur :
        - La culture locale et les coutumes
        - Les meilleures expériences authentiques à vivre
        - Les conseils pratiques (santé, sécurité, déplacements)
        - Les quartiers à explorer
        - La gastronomie locale
        - Les meilleures périodes pour visiter
        - Les horaires d'ouverture des lieux d'intérêt
        - Les événements locaux à ne pas manquer
        
        Excursions et activités :
        - Les meilleures excursions dans le désert au départ d'Essaouira
        - Les options de balades à dos de dromadaire (durée, prix, sécurité)
        - Les autres activités traditionnelles à ne pas manquer
        - Les meilleures périodes pour ces activités
        - Les précautions à prendre pour ces excursions
        - Les opérateurs locaux recommandés""",
        agent=guide_local,
        expected_output="Un rapport détaillé sur la ville, sa culture et les possibilités d'excursions."
    )

    tache_tech = Task(
        description="""Analysez l'écosystème technologique d'Essaouira et du Maroc, en vous concentrant sur :
        - Les acteurs locaux dans le domaine de l'IA
        - Les initiatives liées aux communs numériques
        - Les enjeux de souveraineté technologique
        - Les startups et entreprises tech innovantes
        - Les événements et communautés tech locales
        - Les opportunités de networking dans le domaine tech
        - Les horaires de travail et disponibilités des acteurs tech
        - Les lieux de rencontre habituels de la communauté tech""",
        agent=expert_tech,
        expected_output="Un rapport sur l'écosystème tech local avec identification des acteurs clés et opportunités."
    )

    tache_voyage = Task(
        description="""Créez un itinéraire de voyage complet pour un séjour à Essaouira, incluant :
        - Options de transport depuis Paris (vols, durée, prix approximatifs)
        - Recommandations d'hébergement selon différents budgets
        - Planification des déplacements locaux
        - Suggestions d'itinéraires quotidiens
        - Conseils pratiques pour l'arrivée et le séjour
        - Estimation des budgets nécessaires
        - Informations sur les meilleures périodes pour les activités
        - Conseils sur les réservations nécessaires
        
        Conseils sanitaires et sécurité :
        - Liste complète des vaccins recommandés et obligatoires
        - Autres précautions sanitaires à prendre
        - Conseils pour les excursions dans le désert
        - Kit médical recommandé
        - Numéros d'urgence importants
        - Conseils pour éviter les problèmes de santé courants""",
        agent=expert_voyage,
        expected_output="Un plan de voyage détaillé avec toutes les informations pratiques et sanitaires nécessaires."
    )

    tache_coordination = Task(
        description="""Créez un itinéraire de 5 jours à Essaouira du 20 au 25 avril 2025 en combinant :
        - Les informations culturelles et locales du guide
        - Les opportunités de rencontres tech identifiées
        - Les aspects pratiques du voyage
        - Les recommandations sanitaires
        
        L'itinéraire doit :
        - Équilibrer découverte culturelle et rencontres professionnelles
        - Respecter les horaires d'ouverture des lieux
        - Inclure des temps de repos et de découverte libre
        - Proposer des alternatives en cas de météo défavorable
        - Inclure des recommandations de restaurants et cafés
        - Prévoir des créneaux pour des rencontres tech
        - Suggérer des activités culturelles authentiques
        - Intégrer une excursion dans le désert si possible
        - Inclure les précautions sanitaires et de sécurité nécessaires
        
        Format attendu : 
        - Un planning jour par jour avec horaires, lieux, activités et conseils pratiques
        - Une section spéciale sur les préparatifs sanitaires et de sécurité
        - Des recommandations pour les excursions dans le désert""",
        agent=coordinateur,
        expected_output="Un itinéraire détaillé sur 5 jours combinant culture, tech, aspects pratiques et conseils sanitaires."
    )

    # Créer l'équipe
    crew = Crew(
        agents=[guide_local, expert_tech, expert_voyage, coordinateur],
        tasks=[tache_guide, tache_tech, tache_voyage, tache_coordination],
        verbose=True,
        process=Process.sequential
    )

    # Lancer l'équipe
    result = crew.kickoff()
    print("\nRésultat final :")
    print(result)
    return result

if __name__ == "__main__":
    run_travel_team() 