import folium
import streamlit as st
from streamlit_folium import st_folium
from shapely.geometry import Polygon
from shapely.ops import transform
from pyproj import Transformer

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

# Shapely를 사용하여 다각형 생성
polygon = Polygon(pknu_boundary_coords)

# 좌표 변환 함수 (거리 단위를 미터로 사용하기 위해)
# pyproj의 Transformer를 사용하여 간단히 좌표 변환 설정
transformer_to_utm = Transformer.from_crs('EPSG:4326', 'EPSG:32652', always_xy=True)
transformer_to_wgs84 = Transformer.from_crs('EPSG:32652', 'EPSG:4326', always_xy=True)

# UTM 좌표계로 변환하여 다각형을 25미터 확장
polygon_utm = transform(transformer_to_utm.transform, polygon)
expanded_polygon_utm = polygon_utm.buffer(25)
expanded_polygon = transform(transformer_to_wgs84.transform, expanded_polygon_utm)

# 바깥 경계 좌표 리스트로 변환
expanded_boundary_coords = list(expanded_polygon.exterior.coords)

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

# 부경대 부지 경계 점선 추가 (파란색)
folium.Polygon(
    locations=pknu_boundary_coords,  # 경계선 좌표
    color="blue",  # 선 색깔
    weight=3,      # 선 두께
    dash_array='5, 5',  # 점선 설정 (숫자는 대시 길이와 간격)
    fill=True,  # 폴리곤 내부 채우기 설정
    fill_color='blue',  # 채우기 색상
    fill_opacity=0.2  # 채우기 투명도 (0.0에서 1.0, 낮을수록 더 투명)
).add_to(m)

# 바깥 경계 점선 추가 (확장된 경계선, 초록색)
folium.Polygon(
    locations=expanded_boundary_coords,  # 바깥 경계선 좌표
    color="green",  # 선 색깔
    weight=3,       # 선 두께
    dash_array='5, 5',  # 점선 설정 (숫자는 대시 길이와 간격)
    fill=False      # 바깥 경계는 채우지 않음
).add_to(m)

# 최종 지도를 Streamlit에 표시
out = st_folium(
    m,
    center=center_coords,
    width=1200,
    height=500,
)