from ui import afficher_menu, demander_choix_menu


def main() -> None:
    while True:
        afficher_menu()
        choix = demander_choix_menu()

        if choix == "7":
            print("Au revoir !")
            break
        else:
            print("Option non implémentée pour le moment.")
            input("Appuyez sur Entrée pour revenir au menu...")


if __name__ == "__main__":
    main()