# Q1
def calculer_moyenne_classe(classe):
    if not classe:
        return 0

    somme = 0
    for etudiant in classe:
        moyenne = etudiant["note_cc"] * 0.4 + etudiant["note_examen"] * 0.6
        somme += moyenne
    return somme / len(classe)


# Q2
def mention(note, seuil_passable=10, seuil_bien=14):
    if note < seuil_passable:
        return "AJOURNÉ"
    if note >= seuil_bien:
        return "BIEN"
    return "PASSABLE"


# Q3
def statistiques(notes):
    if not notes:
        return 0, None, None
    return sum(notes) / len(notes), min(notes), max(notes)


# Q4
def compter_notes_validantes(notes):
    compteur = 0
    for note in notes:
        if note >= 10:
            compteur += 1
    return compteur


classe = [
    {"nom": "Amina", "note_cc": 12.0, "note_examen": 15.5},
    {"nom": "Brice", "note_cc": 10.0, "note_examen": 11.0},
    {"nom": "Chloé", "note_cc": 14.0, "note_examen": 16.0},
]
notes = [8, 12, 15, 17, 10, 6]

print(f"Moyenne générale : {calculer_moyenne_classe(classe):.2f}")
for note in notes:
    print(f"Note {note} : {mention(note)}")

moyenne, minimum, maximum = statistiques(notes)
print(f"Statistiques : moyenne={moyenne:.2f}, minimum={minimum}, maximum={maximum}")
print("Notes validantes :", compter_notes_validantes(notes))