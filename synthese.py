import pandas as pd
import random

# Initialize an empty DataFrame
data = pd.DataFrame()

# Generate 1000 rows of data
for _ in range(10_000):
    row = {
        'id': _ + 1,
        'poids (kg)': random.uniform(40, 120),
        'taille (cm)': random.uniform(140, 200),
        'Fréquence cardiaque par minutes': random.randint(50, 100),
        'Tension arterielle systolique matin': random.randint(90, 140),
        'Tension arterielle systolique soir': random.randint(90, 140),
        'Tension arterielle dystolique matin': random.randint(60, 90),
        'Tension arterielle dystolique soir': random.randint(60, 90),
        'Description des symptômes cardio': random.choice(['Aucun', 'Légers', 'Modérés', 'Graves']),
        'Nombres de médicaments': random.randint(0, 10),
        'Oublie prise de medicaments': random.choice(['Non', 'Oui']),
        'Présence d\'effets secondaire': random.choice(['Non', 'Oui']),
        'Symptômes particulier': random.choice(['Aucun', 'Oui']),
        'Description des effets/symptômes rencontré': random.choice(['N/A', 'Douleurs', 'Maux de tête', 'Nausées']),
        'Consommation d\'alcool': random.choice(['Aucune', 'Occasionnelle', 'Fréquente']),
        'Grignotage sucré': random.choice(['Aucun', 'Occasionnel', 'Fréquent']),
        'Grignotage salé': random.choice(['Aucun', 'Occasionnel', 'Fréquent']),
        'Nombre de repas pris dans la journée': random.randint(1, 5),
        'Quantité d\'eau en litre': round(random.uniform(0.5, 3.0), 2),
        'Quantité d\'alcool en litre': round(random.uniform(0, 2.0), 2),
        'Activité physique du jour': random.choice(['Aucune', 'Légère', 'Modérée', 'Intense']),
        'Description de l\'activité': random.choice(['N/A', 'Course', 'Marche', 'Natation']),
        'Durée de l\'activité': random.randint(15, 120),
        'dyspnée': random.choice(['Non', 'Oui']),
        'oedème': random.choice(['Non', 'Oui']),
        'épisodes infectieux': random.choice(['Non', 'Oui']),
        'fièvre': random.choice(['Non', 'Oui']),
        'palpitation': random.choice(['Non', 'Oui']),
        'douleur thoracique': random.choice(['Non', 'Oui']),
        'malaise': random.choice(['Non', 'Oui']),
        'l\'heure du début des palpitation': random.randint(1,24),
        'Durée total des palpitation (minutes)': random.randint(5, 120),
        'l\'heure du début des douleurs thoraciques': random.randint(1,24),
        'Durée total des douleurs thoraciques (minutes)': random.randint(5, 120),
        'l\'heure du début des malaises': random.randint(1,24),
        'Durée total des malaises (minutes)': random.randint(15, 120),
        'Valeurs de natrémie (mmol/l)': random.uniform(100, 200), # valeur uniforme 135 - 145
        'Valeurs de potassim (mmol/l)': random.uniform(2.5, 6.5),
        'Valeurs de créatine (micromol/l)': random.randint(35, 120),
        'Valeurs de clairance de créatine (ml/l)': random.randint(60, 140),
        'Taux de NT Probnp (ng/l)': random.randint(300, 1000),
        'Taux de fer sérique (mg/l)': random.randint(50, 180),
        'Taux d\'hémoglobine (g/100 ml)': random.randint(120, 180),
        'Valeurs de vitesse de sédimentation (mm)': random.randint(10, 60),
        'Taux de protéine C réactive (mg/l)': random.randint(5, 12),
        'Taux de troponine (microgrammes / litre)': random.uniform(0.3, 0.6),
        'Taux de vitamine D (ng/ml de sang)': random.randint(20, 60),
        'Taux d\'acide urique (mg/l)': random.randint(150, 420),
        'Taux de INR (International uniformized Ratio)': random.randint(1, 6),
        # Continue adding more columns as needed...
    }
    data = data._append(row, ignore_index=True)

# Adding columns for the last set of attributes
emotional_attributes = [
    'irritabilité', 'sentiments dépressifs', 'bouche sèche ou gorge sèche', 'actions ou gestes impulsifs',
    'grincement des dents', 'difficulté à rester assis', 'cauchermars', 'diarrhée',
    'attaques verbales envers quelqu\'un', 'hauts et bas émotifs', 'grande envie de pleurer',
    'grande envie de fuir', 'grande envie de faire mal', 'pensées embrouillées', 'débit plus rapide',
    'fatigue ou lourdeur généralisées', 'sentiment d\'être surchargé(e)', 'sentiment d\'être émotivement fragile',
    'sentiment de tristesse', 'sentiment d\'anxiété', 'tension émotionnelle', 'hostilité envers les autres',
    'tremblements ou gestes nerveux', 'bégaiements ou hésitations verbales', 'incapacité ou difficulté à se concentrer',
    'difficulté à organiser ses pensées', 'difficulté à dormir toute la nuit sans se réveiller', 'besoin fréquent d\'uriner',
    'maux d\'estomac ou difficultés à digérer', 'geste ou sentiment d\'impatience', 'maux de tête',
    'douleurs au dos ou à la nuque', 'perte ou gain d\'appétit', 'perte d\'intérêt pour le sexe', 'oublis fréquents',
    'douleurs ou serrements à la poitrine', 'conflits significatifs avec les autres', 'difficultés à se lever après le sommeil',
    'sentiment que les choses sont hors de contrôle', 'difficulté à faire une longue activité continue', 'mouvements de retrait, d\'isolement',
    'difficulté à s\'endormir', 'difficulté à se remettre d\'un événement contrariant', 'mains moites',
    'total de l\'impact du stress dans votre vie actuelle'
]

for attr in emotional_attributes:
    data[attr] = random.randint(0, 10)

# Save the dataset to a CSV file
data.to_csv('health_data.csv', index=False)
