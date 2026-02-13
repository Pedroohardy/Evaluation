# Système de location de véhicules (POO)

## Description des modèles

### Classe Client

Représente un client de l’agence de location.

Attributs :
- id_client (str) : identifiant unique du client (ex: "C001")
- nom (str)
- prenom (str)
- mail (str)
- telephone (str)
- adresse (str)

Rôle :
Permet de stocker les informations personnelles d’un client.


---

### Classe Vehicule

Représente un véhicule disponible à la location.

Attributs :
- id_vehicule (str) : identifiant unique (ex: "V001")
- marque (str)
- modele (str)
- cylindree (int) : 4, 5 ou 6
- kilometrage_actuel (int)
- date_mise_en_circulation (str ou date)

Rôle :
Permet de stocker les caractéristiques d’un véhicule.


---

### Classe Reservation

Représente une réservation effectuée par un client.

Attributs :
- id_reservation (str)
- id_client (str)
- id_vehicule (str)
- date_depart (str, format AAAA-MM-JJ)
- date_retour (str, format AAAA-MM-JJ)
- forfait_km (int : 100, 200, 300 ou +300)
- cout_journalier (float)
- prix_km_supp (float)
- cout_estime (float)

Rôle :
Associe un client à un véhicule sur une période donnée
et calcule un coût estimé.