def afficher_menu() -> None:
    print("=" * 60)
    print("SYSTÈME DE LOCATION DE VÉHICULES")
    print("=" * 60)
    print("1. Afficher les clients")
    print("2. Afficher les véhicules")
    print("3. Créer une réservation")
    print("4. Afficher la grille tarifaire")
    print("5. Afficher toutes les réservations")
    print("6. Afficher les réservations d'un client")
    print("7. Quitter")
    print("=" * 60)


def demander_choix_menu() -> str:
    return input("Votre choix : ").strip()
