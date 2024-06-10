
"""
Prédiction de la biomasse future avec optimisation de la ration alimentaire :
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from scipy.optimize import minimize


# # Prédire la biomasse future sans optimisation de la ration
# predictions_no_opt = model.predict(X_test)

# # Fonction d'objectif pour l'optimisation de la ration alimentaire
# def optimize_ration(r):
#     predicted_biomass = model.predict([[X_test.iloc[0]['Taux de survie (%)'], r]])
#     return -predicted_biomass  # Maximiser la biomasse prédite

# # Contrainte sur la quantité d'aliment
# def constraint_quantity(r):
#     return X_test.iloc[0]['ration'] - r

# # Optimisation de la ration alimentaire
# initial_guess = X_test.iloc[0]['ration'] / 2  # Initialisation avec la moitié de la quantité actuelle
# result = minimize(optimize_ration, initial_guess, constraints={'type': 'ineq', 'fun': constraint_quantity})

# # Prédire la biomasse future avec optimisation de la ration
# optimized_ration = result.x[0]
# predictions_opt = model.predict([[X_test.iloc[0]['Taux de survie (%)'], optimized_ration]])

# # Calculer l'erreur quadratique moyenne (RMSE)
# rmse_no_opt = mean_squared_error(y_test, predictions_no_opt, squared=False)
# rmse_opt = mean_squared_error(y_test, predictions_opt, squared=False)

# print("RMSE sans optimisation:", rmse_no_opt)
# print("RMSE avec optimisation de la ration:", rmse_opt)
# print("Ration optimisée:", optimized_ration)



data = pd.read_excel('JEUX DE_DONNEES_AQUA_CORR.xlsx')

X = data[['Taux de survie (%)', "ration"]]
y = data['Biomasse controlée  (g)']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Entraîner le modèle de régression linéaire
model = LinearRegression()
model.fit(X_train, y_train)

# Prédire le nombre de poissons futur
predictions = model.predict(X_test)

# Calculer l'erreur quadratique moyenne (RMSE)
rmse = mean_squared_error(y_test, predictions, squared=False)
print("RMSE:", rmse)