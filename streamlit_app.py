import streamlit as st
import streamlit.components.v1 as components

# Dictionary of species and corresponding HTML map files
species_maps = {
    "Overall": "multi_species_distribution_with_italicized_legend_filtered.html",
    "Abscondita pallescens": "abscondita_pallescens_male_adults_map.html",
    "Abscondita nr. chinensis": "abscondita_nr_chinensis_male_adult_map.html",
    "Asymmetricata circumdata": "asymmetricata_circumdata_male_adult_map.html",
    "Colophotia brevis": "colophotia_brevis_male_adult_map.html",
    "Curtos costipennis": "curtos_costipennis_male_adult_map.html",
    "Pteroptyx bearni": "pteroptyx_bearni_male_adult_map.html",
    "Pteroptyx malaccae": "pteroptyx_malaccae_male_adult_map.html",
    "Pteroptyx tener": "pteroptyx_tener_male_adult_map.html",
    "Pygoluciola dunguna": "pygoluciola_dunguna_male_adults_map.html"
}

st.set_page_config(page_title="Species Map Viewer", layout="wide")

st.title("Occurrence of Luciolinae Firefly Species in Malaysia")

# Apply custom CSS for the dropdown label to make it italicized
st.markdown("<h4 style='font-style: italic;'>Select a species to view its map:</h4>", unsafe_allow_html=True)

# Dropdown for species selection (label left blank as it's already styled above)
species = st.selectbox(" ", list(species_maps.keys()))  # Empty string in the label

# Display the selected map
map_path = species_maps[species]
with open(map_path, 'r', encoding='utf-8') as f:
    html = f.read()
    components.html(html, height=600, scrolling=True)
