#https://folium.streamlit.app/

import folium
import streamlit as st
from streamlit_folium import st_folium


#부경대 좌표와 지도에서 표시
pknu_latitude = 35.134080249513474
pknu_longitude = 129.10317348438963
pknu = "Pukyong National University - Daeyeon Campus"

# 부경대학교 부지 경계선 좌표
pknu_boundary_coords = [
    [35.13540614195955, 129.10087862006972],  # 점 1
    [35.13601590188572, 129.10857328433084],  # 점 2
    [35.135002467392376, 129.11010486150494],  # 점 3
    [35.13043402505438, 129.10619708232116],  # 점 4
    [35.13073134462104, 129.10594147874792],  # 점 5
    [35.130585105375594, 129.10398518371548],  # 점 6
    [35.131797828489994, 129.10135082088976],  # 점 7
    [35.13540614195955, 129.10087862006972]   # 다시 시작점으로
]

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

#점선 추가
folium.PolyLine(
    locations=pknu_boundary_coords,  # 경계선 좌표
    color="red",  # 선 색깔
    weight=10,      # 선 두께
    dash_array='5, 5'  # 점선 설정 (숫자는 대시 길이와 간격)
).add_to(m)
