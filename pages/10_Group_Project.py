#https://folium.streamlit.app/

import folium
import streamlit as st

from streamlit_folium import st_folium


#부경대 좌표와 지도에서 표시
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


#부경대 영역표시 좌표 검색하기
var feature_group_feature_group_0 = L.featureGroup(
        {}
    );


function geo_json_feature_group_0_0_styler(feature) {
    switch(feature.id) {
        default:
            return {"color": "#ff3939", "dashArray": "5, 5", "fillOpacity": 0, "opacity": 1, "weight": 3};
    }
}

function geo_json_feature_group_0_0_onEachFeature(feature, layer) {
    layer.on({
    });
};
var geo_json_feature_group_0_0 = L.geoJson(null, {
        onEachFeature: geo_json_feature_group_0_0_onEachFeature,

        style: geo_json_feature_group_0_0_styler,
});

function geo_json_feature_group_0_0_add (data) {
    geo_json_feature_group_0_0
        .addData(data);
}
    geo_json_feature_group_0_0_add({"bbox": [-122.397759, 37.794712, -122.396171, 37.795695], "features": [{"bbox": [-122.397759, 37.794712, -122.396171, 37.795695], "geometry": {"coordinates": [[[-122.397416, 37.795017], [-122.397137, 37.794712], [-122.396332, 37.794983], [-122.396171, 37.795483], [-122.396858, 37.795695], [-122.397652, 37.795466], [-122.397759, 37.79511], [-122.397416, 37.795017]]], "type": "Polygon"}, "id": "0", "properties": {}, "type": "Feature"}], "type": "FeatureCollection"});



    geo_json_feature_group_0_0.addTo(feature_group_feature_group_0);


    feature_group_feature_group_0.addTo(map_div);

map_div.addLayer(feature_group_feature_group_0);
window.feature_group = window.feature_group || [];
window.feature_group.push(feature_group_feature_group_0);
