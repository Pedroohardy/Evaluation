class TarifsManager:
    # cylindree -> forfait_km -> (cout_journalier, prix_km_supp)
    TARIFS = {
        4: {
            100: (35.0, 0.25),
            200: (50.0, 0.20),
            300: (65.0, 0.15),
            "+300": (80.0, 0.10)
        },
        5: {
            100: (45.0, 0.30),
            200: (60.0, 0.25),
            300: (75.0, 0.20),
            "+300": (95.0, 0.15)
        },
        6: {
            100: (60.0, 0.40),
            200: (80.0, 0.35),
            300: (100.0, 0.30),
            "+300": (120.0, 0.25)
        }
    }

    @classmethod
    def obtenir_tarif(cls, cylindree, forfait_km):
        return cls.TARIFS[cylindree][forfait_km]

    @classmethod
    def afficher_grille(cls):
        print("=" * 70)
        print("GRILLE TARIFAIRE")
        print("=" * 70)
        print(f"{'Cylindrée':<15}{'Forfait':<10}{'Coût/jour':<15}{'Prix km supp.'}")
        print("-" * 70)

        for cylindree, forfaits in cls.TARIFS.items():
            for forfait, (cout_jour, prix_km) in forfaits.items():
                print(
                    f"{str(cylindree) + ' cylindres':<15}"
                    f"{str(forfait):<10}"
                    f"{cout_jour:<15.2f}€"
                    f"{prix_km:.2f}€/km"
                )
            print("-" * 70)