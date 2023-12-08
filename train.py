import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
from joblib import dump
import seaborn as sns

# Charger le fichier CSV
data = pd.read_csv('C:/Users/vsigogneau/Downloads/penguins-clean-train.csv')

# Diviser les données en features (X) et target (y)
X = data.drop('species', axis=1)
y = data['species']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialiser le modèle k-NN (par exemple, k=3)
knn_model = KNeighborsClassifier(n_neighbors=3)

knn_model.fit(X_train, y_train)

# Évaluer la performance du modèle sur l'ensemble de test
y_pred = knn_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Sauvegarder le modèle entraîné
dump(knn_model, 'knn_model.pkl')
