import streamlit as st
import pandas as pd
import seaborn as sns
import requests

# Charger le jeu de données des pingouins pour obtenir les valeurs uniques de 'sex' et 'island'
penguins = sns.load_dataset('penguins')

# Titre de l'application
st.title('Prédiction des espèces de pingouins')

# Sidebar pour la saisie des valeurs
st.sidebar.header('Saisie des valeurs')
bill_length = st.sidebar.slider('Longueur du bec (mm)', 30.0, 60.0, 40.0)
bill_depth = st.sidebar.slider('Profondeur du bec (mm)', 10.0, 25.0, 15.0)
flipper_length = st.sidebar.slider('Longueur de la nageoire (mm)', 150.0, 250.0, 200.0)
body_mass = st.sidebar.slider('Masse corporelle (g)', 2000.0, 7000.0, 4000.0)

# Créer un dictionnaire avec les valeurs saisies
input_dict = {
    'bill_length_mm': bill_length,
    'bill_depth_mm': bill_depth,
    'flipper_length_mm': flipper_length,
    'body_mass_g': body_mass,
}

# Afficher les valeurs d'entrée
st.subheader('Valeurs d\'entrée:')
st.write(input_dict)

# Bouton de prédiction
if st.button('Prédire'):
    # Faire une requête POST vers le serveur FastAPI
    url = 'http://server:8000/predict'
    response = requests.post(url, json=input_dict)

    # Vérifier si la requête a réussi (code 200 OK)
    if response.status_code == 200:
        # Extraire la prédiction de la réponse JSON
        prediction = response.json()["prediction"]

        # Afficher la prédiction
        st.subheader('Prédiction:')
        st.write(prediction)
    else:
        # Afficher un message d'erreur en cas d'échec de la requête
        st.error(f"Erreur de requête: {response.status_code}")
