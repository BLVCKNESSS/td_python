# Q1
class Etudiant:
    def __init__(self, nom, note_cc, note_examen):
        self.nom = nom
        self.note_cc = note_cc
        self.note_examen = note_examen

    def moyenne(self):
        return self.note_cc * 0.4 + self.note_examen * 0.6

# Q2
def afficher(self):
    print(
    f"{self.nom} — CC : {self.note_cc:.2f} / 20 "
    f"— Examen : {self.note_examen:.2f} / 20"
        )


# Q3
class Groupe:
    def __init__(self):
        self.etudiants = []

    def ajouter(self, etudiant):
        self.etudiants.append(etudiant)

    def moyenne_generale(self):
        if not self.etudiants:
            return 0
        total = sum(etudiant.moyenne() for etudiant in self.etudiants)
        return total / len(self.etudiants)

    def meilleur_etudiant(self):
        if not self.etudiants:
            return None
        return max(self.etudiants, key=lambda etudiant: etudiant.moyenne())


# Q4
class Delegue(Etudiant):
    def __init__(self, nom, note_cc, note_examen, filiere):
        super().__init__(nom, note_cc, note_examen)
        self.filiere = filiere

    def presenter(self):
        return f"Le délégué est {self.nom}, en filière {self.filiere}"


# Q5
groupe = Groupe()
groupe.ajouter(Etudiant("Amina", 12.0, 15.5))
groupe.ajouter(Etudiant("Brice", 10.0, 11.0))
groupe.ajouter(Delegue("Chloé", 14.0, 16.5, "Génie Logiciel"))

for etudiant in groupe.etudiants:
    etudiant.afficher()
    print(f"Moyenne : {etudiant.moyenne():.2f}")

print(f"Moyenne générale : {groupe.moyenne_generale():.2f}")
meilleur = groupe.meilleur_etudiant()
print(f"Meilleure moyenne : {meilleur.nom} avec {meilleur.moyenne():.2f}")