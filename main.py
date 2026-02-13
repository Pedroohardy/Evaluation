from ui import (
    afficher_menu,
    demander_choix_menu,
    afficher_clients,
    afficher_vehicules,
    demander_reservation,
    afficher_reservations,
    afficher_reservations_client,
)
from data_manager import charger_reservations
from models import Reservation


def main() -> None:
    while True:
        afficher_menu()
        choix = demander_choix_menu()

        if choix == "1":
            afficher_clients()

        elif choix == "2":
            afficher_vehicules()

        elif choix == "3":
            demander_reservation()

        elif choix == "5":
            reservations = charger_reservations()
            afficher_reservations(reservations)

        elif choix == "6":
            afficher_reservations_client()

        elif choix == "7":
            print("Au revoir !")
            break

        else:
            print("Option non implémentée.")
            input("Appuyez sur Entrée pour revenir au menu...")


if __name__ == "__main__":
    main()