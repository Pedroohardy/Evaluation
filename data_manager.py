import json
from models import Client, Vehicule, Reservation


def charger_clients():
    with open("clients.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    return [Client.from_dict(client) for client in data]


def charger_vehicules():
    with open("vehicules.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    return [Vehicule.from_dict(vehicule) for vehicule in data]

def charger_reservations():
    with open("reservations.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    reservations = []
    for r in data:
        reservations.append(
            Reservation(
                id_reservation=r["id_reservation"],
                id_client=r["id_client"],
                id_vehicule=r["id_vehicule"],
                date_depart=r["date_depart"],
                date_retour=r["date_retour"],
                forfait_km=r["forfait_km"],
                cout_journalier=r["cout_journalier"],
                prix_km_supp=r["prix_km_supp"],
            )
        )
    return reservations


def generer_id_reservation():
    reservations = charger_reservations()
    if not reservations:
        return "R0001"

    
    max_num = 0
    for r in reservations:
        num = int(r.id_reservation[1:])
        if num > max_num:
            max_num = num

    return f"R{max_num + 1:04d}"


def sauvegarder_reservation(reservation: Reservation):
    reservations = charger_reservations()
    reservations.append(reservation)

    data = [r.to_dict() for r in reservations]

    with open("reservations.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def filtrer_reservations_par_client(id_client: str):
    reservations = charger_reservations()
    return [r for r in reservations if r.id_client == id_client]