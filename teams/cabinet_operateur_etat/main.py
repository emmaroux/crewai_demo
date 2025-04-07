from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
import os

def demander_informations_rdv():
    """Demande à l'utilisateur les informations sur le rendez-vous."""
    print("\n=== Informations sur le rendez-vous ===")
    
    interlocuteur = input("Nom et fonction de l'interlocuteur prioritaire: ")
    objectif = input("Objectif du rendez-vous: ")
    contexte = input("Contexte général (dossier en cours, enjeux, historique): ")
    sujets = input("Sujets spécifiques à aborder: ")
    resultats = input("Résultats attendus: ")
    contraintes = input("Contraintes ou points d'attention particuliers: ")
    niveau_detail = input("Niveau de détail requis pour l'analyse (basique, moyen, approfondi): ")
    
    return {
        "interlocuteur": interlocuteur,
        "objectif": objectif,
        "contexte": contexte,
        "sujets": sujets,
        "resultats": resultats,
        "contraintes": contraintes,
        "niveau_detail": niveau_detail
    }

def run_cabinet_team():
    # Demander les informations sur le rendez-vous
    infos_rdv = demander_informations_rdv()
    
    # Créer les agents
    manager_cabinet = Agent(
        role='Manager de Cabinet',
        goal='Coordonner et cadrer les travaux du cabinet, assurer la cohérence des analyses et recommandations',
        backstory="""Vous êtes un manager de cabinet expérimenté avec une expertise en coordination 
        d'équipes et en gestion de projets stratégiques. Vous avez une vision globale des enjeux 
        institutionnels et opérationnels. Vous savez prioriser les dossiers, coordonner les travaux 
        et assurer la qualité des livrables. Vous avez une excellente capacité d'analyse et de synthèse.
        Votre rôle est également de poser les bonnes questions pour comprendre le contexte d'une recherche
        ou d'un rendez-vous avant de lancer les autres agents.""",
        verbose=True,
        allow_delegation=True
    )

    expert_institutionnel = Agent(
        role='Expert en Acteurs Institutionnels',
        goal='Analyser et comprendre les enjeux et dynamiques des acteurs institutionnels',
        backstory="""Vous êtes un expert en analyse institutionnelle avec une connaissance approfondie 
        des administrations, des collectivités territoriales, des instances de régulation et des 
        organismes publics. Vous maîtrisez les processus décisionnels, les circuits administratifs 
        et les relations inter-institutionnelles. Vous avez une expertise particulière dans 
        l'identification des points de contact clés et des dynamiques de pouvoir.""",
        verbose=True,
        allow_delegation=False
    )

    expert_prive = Agent(
        role='Expert en Acteurs Privés',
        goal='Analyser et comprendre les enjeux et dynamiques des acteurs privés',
        backstory="""Vous êtes un expert en analyse du secteur privé avec une connaissance approfondie 
        des entreprises, des associations, des think tanks et des acteurs économiques. Vous maîtrisez 
        les dynamiques de marché, les stratégies d'entreprise et les relations public-privé. Vous avez 
        une expertise particulière dans l'identification des opportunités de partenariats et des 
        risques potentiels.""",
        verbose=True,
        allow_delegation=False
    )

    expert_bio = Agent(
        role='Expert en Préparation de Biographies',
        goal='Préparer des biographies détaillées et pertinentes des interlocuteurs',
        backstory="""Vous êtes un expert en recherche et analyse biographique avec une expertise 
        particulière dans l'identification des opinions, positions et actualités des personnalités. 
        Vous maîtrisez les techniques de veille et d'analyse de contenu. Vous savez identifier les 
        points d'attention et les sujets sensibles. Vous avez une excellente capacité à synthétiser 
        l'information et à mettre en perspective les éléments clés.""",
        verbose=True,
        allow_delegation=False
    )

    # Tâche initiale pour le manager - synthétiser le contexte
    tache_synthese_contexte = Task(
        description=f"""En tant que manager de cabinet, vous devez synthétiser le contexte du rendez-vous 
        basé sur les informations suivantes :
        
        Interlocuteur prioritaire: {infos_rdv['interlocuteur']}
        Objectif du rendez-vous: {infos_rdv['objectif']}
        Contexte général: {infos_rdv['contexte']}
        Sujets à aborder: {infos_rdv['sujets']}
        Résultats attendus: {infos_rdv['resultats']}
        Contraintes ou points d'attention: {infos_rdv['contraintes']}
        Niveau de détail requis: {infos_rdv['niveau_detail']}
        
        Format attendu :
        - Une synthèse structurée du contexte
        - Des recommandations sur la direction à prendre
        - Des points d'attention particuliers""",
        agent=manager_cabinet,
        expected_output="Une synthèse du contexte et des informations clés pour guider les autres agents."
    )

    # Créer les tâches
    tache_analyse_institutionnelle = Task(
        description=f"""Analysez les enjeux et dynamiques des acteurs institutionnels pertinents pour 
        le dossier en cours, en tenant compte du contexte suivant :
        
        Interlocuteur: {infos_rdv['interlocuteur']}
        Objectif: {infos_rdv['objectif']}
        Contexte: {infos_rdv['contexte']}
        Sujets: {infos_rdv['sujets']}
        
        Fournissez :
        - Une cartographie des acteurs clés
        - Les enjeux et positions de chacun
        - Les dynamiques de pouvoir et d'influence
        - Les points de vigilance et opportunités
        - Les recommandations de positionnement
        - Les points de contact stratégiques
        
        Format attendu :
        - Une analyse structurée par acteur
        - Des recommandations concrètes
        - Des points d'attention particuliers""",
        agent=expert_institutionnel,
        expected_output="Une analyse détaillée des acteurs institutionnels avec recommandations."
    )

    tache_analyse_privee = Task(
        description=f"""Analysez les enjeux et dynamiques des acteurs privés pertinents pour 
        le dossier en cours, en tenant compte du contexte suivant :
        
        Interlocuteur: {infos_rdv['interlocuteur']}
        Objectif: {infos_rdv['objectif']}
        Contexte: {infos_rdv['contexte']}
        Sujets: {infos_rdv['sujets']}
        
        Fournissez :
        - Une cartographie des acteurs privés clés
        - Les enjeux économiques et stratégiques
        - Les opportunités de partenariats
        - Les risques potentiels
        - Les recommandations de positionnement
        - Les points de contact stratégiques
        
        Format attendu :
        - Une analyse structurée par acteur
        - Des recommandations concrètes
        - Des points d'attention particuliers""",
        agent=expert_prive,
        expected_output="Une analyse détaillée des acteurs privés avec recommandations."
    )

    tache_preparation_bio = Task(
        description=f"""Préparez une biography détaillée de l'interlocuteur prioritaire, en tenant compte 
        du contexte suivant :
        
        Interlocuteur: {infos_rdv['interlocuteur']}
        Objectif: {infos_rdv['objectif']}
        Contexte: {infos_rdv['contexte']}
        Sujets: {infos_rdv['sujets']}
        Niveau de détail requis: {infos_rdv['niveau_detail']}
        
        Incluez :
        - Parcours professionnel et responsabilités actuelles
        - Positions et opinions sur les sujets clés
        - Actualités récentes et engagements
        - Points de vigilance et sujets sensibles
        - Opportunités de dialogue
        - Recommandations pour l'entretien
        
        Format attendu :
        - Une synthèse biographique
        - Les points d'attention particuliers
        - Des recommandations concrètes pour l'entretien""",
        agent=expert_bio,
        expected_output="Une biography détaillée avec recommandations pour l'entretien."
    )

    tache_coordination = Task(
        description=f"""Coordonnez les travaux et préparez une synthèse globale incluant :
        - Synthèse des analyses institutionnelles et privées
        - Points clés de la biography
        - Recommandations stratégiques globales
        - Points d'attention particuliers
        - Ordre du jour recommandé pour la réunion
        - Messages clés à porter
        
        Contexte du rendez-vous :
        Interlocuteur: {infos_rdv['interlocuteur']}
        Objectif: {infos_rdv['objectif']}
        Contexte: {infos_rdv['contexte']}
        Sujets: {infos_rdv['sujets']}
        Résultats attendus: {infos_rdv['resultats']}
        Contraintes: {infos_rdv['contraintes']}
        
        Format attendu :
        - Une synthèse structurée
        - Un ordre du jour détaillé
        - Des recommandations concrètes
        - Des points de vigilance""",
        agent=manager_cabinet,
        expected_output="Une synthèse globale avec ordre du jour et recommandations."
    )

    # Créer l'équipe
    crew = Crew(
        agents=[manager_cabinet, expert_institutionnel, expert_prive, expert_bio],
        tasks=[tache_synthese_contexte, tache_analyse_institutionnelle, tache_analyse_privee, tache_preparation_bio, tache_coordination],
        verbose=True,
        process=Process.sequential
    )

    # Lancer l'équipe
    result = crew.kickoff()
    print("\nRésultat final :")
    print(result)
    return result

if __name__ == "__main__":
    run_cabinet_team() 