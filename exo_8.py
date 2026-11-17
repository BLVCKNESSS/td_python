# Q1
etudiant = {
    "nom": "Amina",
    "age": 20,
    "filiere": "Génie Logiciel",
    "moyenne": 14.3,
}

for cle, valeur in etudiant.items():
    print(f"{cle} : {valeur}")

# Q2
classe = [
    {"nom": "Amina", "note_cc": 12.0, "note_examen": 15.5},
    {"nom": "Brice", "note_cc": 10.0, "note_examen": 11.0},
    {"nom": "Chloé", "note_cc": 14.0, "note_examen": 16.0},
]

somme_moyennes = 0
for personne in classe:
    moyenne = personne["note_cc"] * 0.4 + personne["note_examen"] * 0.6
    somme_moyennes += moyenne
    print(f"{personne['nom']} : {moyenne:.2f} / 20")

moyenne_classe = somme_moyennes / len(classe)
print(f"Moyenne générale de la classe : {moyenne_classe:.2f} / 20")

# Q3
bulletins = [
    ("Amina", 10.5, 17.5, 14.2),
    ("Brice", 8.0, 15.0, 11.5),
    ("Chloé", 12.0, 18.5, 15.8),
]

for nom, note_min, note_max, moyenne in bulletins:
    print(f"{nom} — écart : {note_max - note_min:.2f}, moyenne : {moyenne:.2f}")

# Q4
mention = etudiant.get("mention", "aucune")
print("Mention :", mention)