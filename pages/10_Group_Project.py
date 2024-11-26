#https://folium.streamlit.app/

import folium
import streamlit as st
from streamlit_folium import st_folium
from geopy.distance import geodesic
import math

# 부경대 좌표와 지도에서 표시
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

# 바깥 경계선 좌표 생성 (각 좌표에서 25m 바깥으로 이동)
expanded_boundary_coords = []

for i in range(len(pknu_boundary_coords)):
    # 현재 좌표와 다음 좌표
    current_point = pknu_boundary_coords[i]
    next_point = pknu_boundary_coords[(i + 1) % len(pknu_boundary_coords)]

    # 현재 좌표에서 다음 좌표로 가는 방향의 각도 계산
    delta_lat = next_point[0] - current_point[0]
    delta_lon = next_point[1] - current_point[1]
    angle = math.atan2(delta_lat, delta_lon)
    bearing = math.degrees(angle)

    # 현재 점에서 바깥쪽으로 25미터 이동
    expanded_point = geodesic(meters=25).destination((current_point[0], current_point[1]), bearing)
    expanded_boundary_coords.append([expanded_point.latitude, expanded_point.longitude])

# 지도 생성
m = folium.Map(location=[pknu_latitude, pknu_longitude], zoom_start=15)

# 클릭하면 좌표 표시
m.add_child(folium.LatLngPopup())

# 부경대 마커 추가
folium.Marker(
    location=[pknu_latitude, pknu_longitude],
    popup=pknu,
    icon=folium.Icon(color='red', icon='star')
).add_to(m)

# 부경대 부지 경계 점선 추가
folium.Polygon(
    locations=pknu_boundary_coords,  # 경계선 좌표
    color="blue",  # 선 색깔
    weight=3,      # 선 두께
    dash_array='5, 5',  # 점선 설정 (숫자는 대시 길이와 간격)
    fill=True,  # 폴리곤 내부 채우기 설정
    fill_color='blue',  # 채우기 색상
    fill_opacity=0.2  # 채우기 투명도 (0.0에서 1.0, 낮을수록 더 투명)
).add_to(m)

# 바깥 경계 점선 추가 (확장된 경계선)
folium.Polygon(
    locations=expanded_boundary_coords,  # 바깥 경계선 좌표
    color="green",  # 선 색깔
    weight=3,       # 선 두께
    dash_array='5, 5',  # 점선 설정 (숫자는 대시 길이와 간격)
    fill=False      # 바깥 경계는 채우지 않음
).add_to(m)


# 최종 지도 업데이트
# 뭔가 작성하려면 이 위로 작성 할 것.
out = st_folium(
    m,
    center=center_coords,
    width=1200,
    height=500,
)