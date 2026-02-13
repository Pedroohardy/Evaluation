class Reservation:
    def __init__(
        self,
        id_reservation: str,
        id_client: str,
        id_vehicule: str,
        date_depart: str,
        date_retour: str,
        forfait_km,
        cout_journalier: float,
        prix_km_supp: float,
        cout_estime: float,
    ) -> None:
        self.id_reservation = id_reservation
        self.id_client = id_client
        self.id_vehicule = id_vehicule
        self.date_depart = date_depart
        self.date_retour = date_retour
        self.forfait_km = forfait_km
        self.cout_journalier = cout_journalier
        self.prix_km_supp = prix_km_supp
        self.cout_estime = cout_estime

    def __str__(self) -> str:
        return (
            f"{self.id_reservation} | "
            f"Client: {self.id_client} | "
            f"Véhicule: {self.id_vehicule} | "
            f"{self.date_depart} ➔ {self.date_retour} | "
            f"Forfait: {self.forfait_km} km | "
            f"Coût estimé: {self.cout_estime:.2f}€"
        )

    def to_dict(self) -> dict:
        return {
            "id_reservation": self.id_reservation,
            "id_client": self.id_client,
            "id_vehicule": self.id_vehicule,
            "date_depart": self.date_depart,
            "date_retour": self.date_retour,
            "forfait_km": self.forfait_km,
            "cout_journalier": self.cout_journalier,
            "prix_km_supp": self.prix_km_supp,
            "cout_estime": self.cout_estime,
        }