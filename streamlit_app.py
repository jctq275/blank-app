import streamlit as st
import streamlit.components.v1 as components

# Dictionary of species and corresponding HTML map files
species_maps = {
    "Abscondita pallescens": "/Users/jeromechan/Downloads/abscondita_pallescens_male_adults_map.html",
    "Abscondita nr. chinensis": "/Users/jeromechan/Downloads/abscondita_nr_chinensis_male_adult_map.html",
    "Asymmetricata circumdata": "/Users/jeromechan/Downloads/asymmetricata_circumdata_male_adult_map.html",
    "Colophotia brevis": "/Users/jeromechan/Downloads/colophotia_brevis_male_adult_map.html",
    "Curtos costipennis": "/Users/jeromechan/Downloads/curtos_costipennis_male_adult_map.html",
    "Pteroptyx bearni": "/Users/jeromechan/Downloads/pteroptyx_bearni_male_adult_map.html",
    "Pteroptyx malaccae": "/Users/jeromechan/Downloads/pteroptyx_malaccae_male_adult_map.html",
    "Pteroptyx tener": "/Users/jeromechan/Downloads/pteroptyx_tener_male_adult_map.html",
    "Pygoluciola dunguna": "/Users/jeromechan/Downloads/pygoluciola_dunguna_male_adults_map.html"
}

st.set_page_config(page_title="Species Map Viewer", layout="wide")

st.title("🗺️ Interactive Species Map Viewer")

# Dropdown for species selection
species = st.selectbox("Select a species to view its map:", list(species_maps.keys()))

# Display the selected map
map_path = species_maps[species]
with open(map_path, 'r', encoding='utf-8') as f:
    html = f.read()
    components.html(html, height=600, scrolling=True)
