#https://folium.streamlit.app/

import folium
import streamlit as st

from streamlit-folium import st_folium


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

m.add_child(folium.LatLngPopup()) 



#부경대 영역표시 Dynamic layer control
var map_div = L.map(
    "map_div",
    {
        center: [north, east],
        crs: L.CRS.EPSG3857,
        zoom: 17,
        zoomControl: true,
        preferCanvas: false,
    }
);

var tile_layer_div_0 = L.tileLayer(
    "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
    {"attribution": "\u0026copy; \u003ca href=\"https://www.openstreetmap.org/copyright\"\u003eOpenStreetMap\u003c/a\u003e contributors", "detectRetina": false, "maxNativeZoom": 19, "maxZoom": 21, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
);


tile_layer_div_0.addTo(map_div);

var drawnItems = [];

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
    geo_json_feature_group_0_0_add({"bbox": [-122.397759, 37.794712, -122.396171, 37.795695], "features": [{"bbox": [-122.397759, 37.794712, -122.396171, 37.795695], "geometry": {"coordinates": [[[35.13537883403971, 129.10089437313093], [35.13601158899595, 129.10856220310063], [35.135002276392, 129.11011582641603], [35.12992811181822, 129.10562188009783], [35.131749730479164, 129.1013962047231 ]]], "type": "Polygon"}, "id": "0", "properties": {}, "type": "Feature"}], "type": "FeatureCollection"});



    geo_json_feature_group_0_0.addTo(feature_group_feature_group_0);


    feature_group_feature_group_0.addTo(map_div);

map_div.addLayer(feature_group_feature_group_0);
window.feature_group = window.feature_group || [];
window.feature_group.push(feature_group_feature_group_0);
