# Importation des bibliothèques nécessaires
import os
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler


from deep_translator import GoogleTranslator
translator = GoogleTranslator(source='auto', target='fr')

# Ajout d'un fond d'écran

page_element="""
<style>
[data-testid="stAppViewContainer"]{
  background-image: url("https://lafibre.info/images/smileys/201004_Warm_lights_by_Max_Barners.jpg");
  background-size: cover;
}
</style>
"""

st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mpeg", autoplay=False)


st.markdown(page_element, unsafe_allow_html=True)


# Création d'un menu permettant d'accéder à la page d'accueil ou d'accéder à deux stratégies différentes de choix du film


#option = st.radio("Quelle page de notre application souhaiteriez-vous consulter ?", 
                  #["Accueil", "Choix par acteur", "Choix par genre et par période"])


# CSS pour personnaliser les boutons (texte en blanc et en gras)
st.markdown("""
    <style>
        /* Personnaliser le texte des boutons pour les rendre blancs et en gras */
        .stButton>button {
            background-color: transparent !important;  /* Fond transparent */
            color: white !important;  /* Texte blanc */
            font-weight: bold !important;  /* Texte en gras */
            border: 2px solid white !important;  /* Bordure blanche */
            padding: 15px;  /* Taille du bouton */
            font-size: 18px;  /* Taille du texte */
            width: 100%;  /* Largeur complète pour centrer */
        }

        /* Appliquer un style au hover des boutons pour un effet visuel */
        .stButton>button:hover {
            background-color: white !important;  /* Changer le fond au survol */
            color: #4CAF50 !important;  /* Changer la couleur du texte au survol */
        }

        /* Centrer les titres */
        h1 {
            text-align: center !important;
            color: white !important;
        }

        /* Centrer le texte des paragraphes (st.write) */
        .stMarkdown p {
            text-align: center !important;
            color: white !important;
        }

        /* Personnaliser le texte global en blanc */
        body {
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Créer une ligne de colonnes (menu horizontal)
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])  # Colonnes de largeur égale

with col1:
    if st.button("Accueil"):
        option1 = True
    else:
        option1 = False

with col2:
    if st.button("Choix par acteur"):
        option2 = True
    else:
        option2 = False

with col3:
    if st.button("Choix par genre et par période"):
        option3 = True
    else:
        option3 = False
with col4:
    if st.button("Choix similaires à votre film préféré"):
        option4 = True
    else:
        option4 = False

# Affichage du contenu en fonction de l'option sélectionnée
if option1 or not (option2 or option3 or option4):  # Si aucune option n'est sélectionnée, afficher la page d'accueil
    st.markdown(
        """
        <h1 style="color: white; text-align: center;">Bienvenue sur l'application de recommandations</h1>
        <h2 style="color: orange; text-align: center;">Offerte par votre cinéma ! </h2>
        """, unsafe_allow_html=True
    )
elif option2:
    st.title("Choix par acteur")
    st.write("Choisissez un acteur, nous pourrez apprécier quelques recommandations.")
elif option3:
    st.title("Choix par genre et par période")
    st.write("Choisissez un genre et une période, nous pourrez apprécier quelques recommandations.")
elif option4:
    st.title("Recommandation de films similaires à votre choix")
    st.write("Choisissez un film, nous pourrez apprécier des recommandations sur des films similaires.")
