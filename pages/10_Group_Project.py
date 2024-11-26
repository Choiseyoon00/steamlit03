import folium
import streamlit as st

from streamlit_folium import st_folium

north = 35.134080249513474
east = 129.10317348438963
location_name = "Pukyong National University - Daeyeon Campus"

# center on PKNU, add marker
m = folium.Map(
    location=[north, east],
    zoom_start=15
)
folium.Marker(
  location=[north, east],
  popup=location_name,
  icon=folium.Icon(color='red',icon='star')
).add_to(m)

st_data = st_folium(m, width=725)
