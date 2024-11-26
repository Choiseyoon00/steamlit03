#https://folium.streamlit.app/

import folium
import streamlit as st
from streamlit_folium import st_folium


#부경대 좌표와 지도에서 표시
pknu_latitude = 35.134080249513474
pknu_longitude = 129.10317348438963
pknu = "Pukyong National University - Daeyeon Campus"

# center on PKNU, add marker
m = folium.Map(
    location=[pknu_latitude, pknu_longitude],
    zoom_start=15
)

#클릭하면 좌표 표시
m.add_child(folium.LatLngPopup()) 

folium.Marker(
  location=[pknu_latitude, pknu_longitude],
  popup=pknu,
  icon=folium.Icon(color='red',icon='star')
).add_to(m)

st_data = st_folium(m, width=725)

m.add_child(folium.LatLngPopup()) 

