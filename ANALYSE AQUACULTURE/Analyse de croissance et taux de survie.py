
import pandas as pd

# Charger les données depuis le fichier Excel
data = pd.read_excel('donnees_croissance_survie.xlsx')

# Calculer la croissance journalière
data['Croissance_journaliere'] = (data['Poids_moyen_controle'] - data['Poids_moyen_initial']) / data['TCA']

# Calculer le taux de croissance spécifique
data['Taux_croissance_specifique'] = ((data['Poids_moyen_controle'] - data['Poids_moyen_initial']) / data['Poids_moyen_initial']) * 100

# Calculer le taux de survie
data['Taux_survie'] = (data['Nombre_individu_controle'] / data['Nombre_individu_initial']) * 100

# Afficher les résultats
print(data[['Bacs', 'Croissance_journaliere', 'Taux_croissance_specifique', 'Taux_survie']])
