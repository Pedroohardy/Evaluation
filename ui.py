import os

def nettoyer_terminal() -> None:
    os.system("cls" if os.name == "nt" else "clear")

from datetime import datetime


from data_manager import (
    charger_clients,
    charger_vehicules,
    generer_id_reservation,
    sauvegarder_reservation,
)
from models import TarifsManager, Reservation

from data_manager import charger_reservations, filtrer_reservations_par_client


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


def afficher_clients() -> None:
    print("=" * 60)
    print("LISTE DES CLIENTS")
    print("=" * 60)

    clients = charger_clients()
    for client in clients:
        print(client)

    print("=" * 60)
    input("Appuyez sur Entrée pour revenir au menu...")


def afficher_vehicules() -> None:
    print("=" * 60)
    print("LISTE DES VÉHICULES")
    print("=" * 60)

    vehicules = charger_vehicules()
    for vehicule in vehicules:
        print(vehicule)

    print("=" * 60)
    input("Appuyez sur Entrée pour revenir au menu...")


def afficher_recapitulatif(reservation: Reservation) -> None:
    print("=" * 60)
    print("RÉCAPITULATIF DE LA RÉSERVATION")
    print("=" * 60)
    print(f"Réservation {reservation.id_reservation}")
    print(f"Client: {reservation.id_client}")
    print(f"Véhicule: {reservation.id_vehicule}")
    print(f"Du {reservation.date_depart} au {reservation.date_retour}")
    print(f"Forfait: {reservation.forfait_km} km")
    print(f"Coût journalier: {reservation.cout_journalier:.2f}€")
    print(f"Prix km supp.: {reservation.prix_km_supp:.2f}€/km")
    print(f"Coût estimé: {reservation.cout_estime:.2f}€")
    print("=" * 60)


def _pause():
    input("Appuyez sur Entrée pour revenir au menu...")


def _date_valide(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def _forfait_valide(val: str) -> bool:
    return val in {"100", "200", "300", "+300"}

def demander_reservation() -> None:
    print("=" * 60)
    print("CRÉER UNE NOUVELLE RÉSERVATION")
    print("=" * 60)

    clients = charger_clients()
    vehicules = charger_vehicules()

    print("Clients disponibles :")
    for c in clients:
        print(f"- {c}")

    id_client = input("ID du client : ").strip()

    client_sel = next((c for c in clients if c.id_client == id_client), None)
    if client_sel is None:
        print("❌ Client inexistant.")
        _pause()
        return

    print("Véhicules disponibles :")
    for v in vehicules:
        print(f"- {v}")

    id_vehicule = input("ID du véhicule : ").strip()

    vehicule_sel = next((v for v in vehicules if v.id_vehicule == id_vehicule), None)
    if vehicule_sel is None:
        print("❌ Véhicule inexistant.")
        _pause()
        return

    date_depart = input("Date de départ (AAAA-MM-JJ) : ").strip()
    if not _date_valide(date_depart):
        print("❌ Format de date invalide.")
        _pause()
        return

    date_retour = input("Date de retour (AAAA-MM-JJ) : ").strip()
    if not _date_valide(date_retour):
        print("❌ Format de date invalide.")
        _pause()
        return

    d1 = datetime.strptime(date_depart, "%Y-%m-%d").date()
    d2 = datetime.strptime(date_retour, "%Y-%m-%d").date()

    if d2 <= d1:
        print("❌ La date de retour doit être après la date de départ.")
        _pause()
        return

    print("Forfaits disponibles : 100, 200, 300, +300")
    forfait_saisie = input("Forfait kilométrique : ").strip()

    if not _forfait_valide(forfait_saisie):
        print("❌ Forfait invalide.")
        _pause()
        return

    forfait = "+300" if forfait_saisie == "+300" else int(forfait_saisie)

    try:
        cout_journalier, prix_km_supp = TarifsManager.obtenir_tarif(
            vehicule_sel.cylindree,
            forfait
        )
    except KeyError:
        print("❌ Tarif introuvable.")
        _pause()
        return

    reservation = Reservation(
        id_reservation=generer_id_reservation(),
        id_client=id_client,
        id_vehicule=id_vehicule,
        date_depart=date_depart,
        date_retour=date_retour,
        forfait_km=forfait,
        cout_journalier=cout_journalier,
        prix_km_supp=prix_km_supp,
    )

    afficher_recapitulatif(reservation)

    choix = input("Sauvegarder cette réservation ? (o/n) : ").strip().lower()
    if choix == "o":
        sauvegarder_reservation(reservation)
        print("✓ Réservation sauvegardée.")
    else:
        print("Réservation annulée.")

    _pause()




def afficher_reservations(reservations) -> None:
    print("=" * 60)
    print("LISTE DES RÉSERVATIONS")
    print("=" * 60)

    if not reservations:
        print("Aucune réservation.")
    else:
        for r in reservations:
            print(r)

    print("=" * 60)
    input("Appuyez sur Entrée pour revenir au menu...")


def demander_id_client() -> str:
    return input("ID du client à rechercher : ").strip()


def afficher_reservations_client() -> None:
    id_client = demander_id_client()
    reservations = filtrer_reservations_par_client(id_client)

    print("=" * 60)
    print(f"RÉSERVATIONS DU CLIENT {id_client}")
    print("=" * 60)

    if not reservations:
        print("Aucune réservation pour ce client.")
    else:
        for r in reservations:
            print(r)

    print("=" * 60)
    input("Appuyez sur Entrée pour revenir au menu...")