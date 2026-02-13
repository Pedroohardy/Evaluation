import json
from models.client import Client
from models.vehicule import Vehicule


def charger_clients():
    with open("clients.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    return [Client.from_dict(client) for client in data]


def charger_vehicules():
    with open("vehicules.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    return [Vehicule.from_dict(vehicule) for vehicule in data]

