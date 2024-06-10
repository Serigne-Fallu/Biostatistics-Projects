
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_excel('JEUX DE_DONNEES_AQUA_CORR.xlsx')

correlation = data[['Ration (g)', 'Gain Pm absolu (g) ', 'Biomasse controlée  (g)']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Corrélation entre les variables d\'alimentation et les variables de croissance')
plt.show()

sns.scatterplot(x='Ration (g)', y='Biomasse controlée  (g)', data=data)
plt.xlabel('Ration alimentaire')
plt.ylabel('Biomasse')
plt.title('Influence de la ration alimentaire sur la biomasse')
plt.show()
