import folium
import streamlit as st

from streamlit_folium import st_folium

north = 35.1340
east = 129.1032
location_name = "Pukyong National University - Daeyeon Campus"


# center on Liberty Bell, add marker
m = folium.Map(location=[north, east], zoom_start=16)
folium.Marker(
    [north, east], popup=location_name, tooltip=location_name
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)
