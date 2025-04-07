from dotenv import load_dotenv
import os
from teams.travel_team.main import run_travel_team
from teams.cabinet_operateur_etat.main import run_cabinet_team
# Nous importerons d'autres équipes ici au fur et à mesure

def main():
    # Charger les variables d'environnement
    load_dotenv()
    
    # Menu simple pour choisir quelle équipe exécuter
    print("\n=== CrewAI Enterprise ===")
    print("1. Équipe Voyage (Essaouira)")
    print("2. Équipe Cabinet Opérateur d'État")
    print("3. Quitter")
    
    choice = input("\nChoisissez une équipe à exécuter (1-3): ")
    
    if choice == "1":
        print("\nLancement de l'équipe Voyage...")
        run_travel_team()
    elif choice == "2":
        print("\nLancement de l'équipe Cabinet Opérateur d'État...")
        run_cabinet_team()
    elif choice == "3":
        print("\nAu revoir!")
    else:
        print("\nChoix invalide!")

if __name__ == "__main__":
    main() 