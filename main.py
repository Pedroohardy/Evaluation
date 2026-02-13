from ui import (
    afficher_menu,
    demander_choix_menu,
    afficher_clients,
    afficher_vehicules,
    demander_reservation,
    afficher_reservations,
    afficher_reservations_client,
    nettoyer_terminal,
)
from data_manager import charger_reservations
from models import Reservation


def main() -> None:
    while True:
        nettoyer_terminal()
        afficher_menu()
        choix = demander_choix_menu()

        if choix == "1":
            nettoyer_terminal()
            afficher_clients()

        elif choix == "2":
            nettoyer_terminal()
            afficher_vehicules()

        elif choix == "3":
            nettoyer_terminal()
            demander_reservation()

        elif choix == "5":
            nettoyer_terminal()
            reservations = charger_reservations()
            afficher_reservations(reservations)

        elif choix == "6":
            nettoyer_terminal()
            afficher_reservations_client()

        elif choix == "7":
            print("Au revoir !")
            break

        else:
            print("Option non implémentée.")
            input("Appuyez sur Entrée pour revenir au menu...")


if __name__ == "__main__":
    main()