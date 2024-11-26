import folium
import streamlit as st

from streamlit_folium import st_folium

# center on Liberty Bell, add marker
m = folium.Map(location=[35.1340, 129.1032], zoom_start=16)
folium.Marker(
    [35.1340, 129.1032], popup="Pukyong National University (PKNU) - Daeyeon Campus", tooltip="Pukyong National University (PKNU) - Daeyeon Campus"
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)
