# Q1
import matplotlib.pyplot as plt

evaluations = [f"Éval {i}" for i in range(1, 11)]
notes = [12.5, 14.0, 13.5, 16.0, 15.5, 14.8, 17.0, 16.2, 15.0, 18.0]

plt.plot(evaluations, notes)
plt.title("Évolution des notes")
plt.xlabel("Évaluation")
plt.ylabel("Note (/20)")

# Q2
moyennes_glissantes = []
for i in range(len(notes)):
    debut = max(0, i - 2)
    fenetre = notes[debut:i + 1]
    moyennes_glissantes.append(sum(fenetre) / len(fenetre))

plt.plot(
    evaluations,
    moyennes_glissantes,
    linestyle="--",
    label="Moyenne glissante sur 3 évaluations",
)
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# Q3
filieres = ["Génie Logiciel", "Réseaux", "Gestion", "Marketing", "Logistique"]
effectifs = [42, 35, 28, 31, 24]

plt.figure(figsize=(9, 4))
plt.bar(filieres, effectifs, color="#2e75b6")
plt.title("Effectifs par filière")
plt.xlabel("Filière")
plt.ylabel("Nombre d'étudiants")
plt.show()

# Q4
semaines = list(range(1, 13))
notes_semaines = [12.5, 14.0, 13.5, 16.0, 15.5, 14.8, 17.0, 16.2, 15.0, 18.0, 16.8, 17.5]
presences = [95, 92, 88, 90, 94, 96, 89, 91, 93, 87, 94, 97]

fig, axes = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
axes[0].plot(semaines, notes_semaines)
axes[0].set_title("Notes et présence")
axes[0].set_ylabel("Note (/20)")
axes[0].grid(alpha=0.3)

axes[1].bar(semaines, presences, color="#2e75b6")
axes[1].set_ylabel("Présence (%)")
axes[1].set_xlabel("Semaine")
plt.tight_layout()
plt.show()

# Q5
import seaborn as sns

sns.set_theme(style="whitegrid")
sns.histplot(notes, bins=5, kde=True, color="#2e75b6")
plt.title("Distribution des notes")
plt.xlabel("Note (/20)")
plt.show()

# Q6
import pandas as pd

notes_df = pd.DataFrame({
    "Maths": [12, 14, 10, 15, 11, 16, 13, 9, 17, 14],
    "Algo": [15, 16, 11, 14, 13, 17, 12, 10, 16, 15],
    "Réseaux": [11, 13, 12, 16, 10, 14, 15, 12, 13, 17],
})

corr = notes_df.corr()
sns.heatmap(corr, annot=True, cmap="Blues", fmt=".2f", square=True)
plt.title("Corrélation entre les notes des matières")
plt.show()
