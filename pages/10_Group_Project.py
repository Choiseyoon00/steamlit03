#https://folium.streamlit.app/

import folium
import streamlit as st
from streamlit_folium import st_folium


#부경대 좌표와 지도에서 표시
pknu_latitude = 35.1329
pknu_longitude = 129.1038
center_coords = [pknu_latitude, pknu_longitude]
pknu = "Pukyong National University - Daeyeon Campus"

# 부경대학교 부지 경계선 좌표
pknu_boundary_coords = [
    [35.135406, 129.100878],  # 점 1
    [35.136015, 129.108573],  # 점 2
    [35.135002, 129.110104],  # 점 3
    [35.130434, 129.106197],  # 점 4
    [35.130731, 129.105941],  # 점 5
    [35.130585, 129.103985],  # 점 6
    [35.131797, 129.101350],  # 점 7
    [35.135406, 129.100878]   # 다시 시작점으로
]

# 지도 생성
m = folium.Map(location=[pknu_latitude, pknu_longitude], zoom_start=15)

#클릭하면 좌표 표시
m.add_child(folium.LatLngPopup()) 

#부경대 마커
folium.Marker(
  location=[pknu_latitude, pknu_longitude],
  popup=pknu,
  icon=folium.Icon(color='red',icon='star')
).add_to(m)

#부경대 부지 경계 점선
folium.Polygon(
    locations=pknu_boundary_coords,  # 경계선 좌표
    color="blue",  # 선 색깔
    weight=3,      # 선 두께
    dash_array='5, 5'  # 점선 설정 (숫자는 대시 길이와 간격)
    fill=True,  # 폴리곤 내부 채우기 설정
    fill_color='blue',  # 채우기 색상
    fill_opacity=0.2  # 채우기 투명도 (0.0에서 1.0, 낮을수록 더 투명)
).add_to(m)


out = st_folium(
    m,
    center=center_coords,
    width=1200,
    height=500,
)