
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_excel('JEUX DE_DONNEES_AQUA_CORR.xlsx')

data_cont = data.drop(["Date", "Aliment", "Bacs"], axis=1)

correlation = data_cont.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Corrélation entre les variables')
plt.show()

sns.pairplot(data_cont, x_vars=['Biomasse controlée  (g)', 'Ration (g)', 'Taux de survie (%)',"ration ind" ,"TCA"], 
             y_vars=['Taux de croissance spécifique (% en j)'],kind='reg', height=5)
plt.show()
