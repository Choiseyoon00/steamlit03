import requests
import plotly.graph_objects as go
from streamlit import session_state as ss
import streamlit as st

key=AIzaSyAYbxJm_JxPYaoxw0c-bsP1hDONYcFnQrw

def get_session_url(api_key):
    create_session_url = "https://tile.googleapis.com/v1/createSession"

    payload = {
        "mapType": "satellite",
        "language": "en-US",
        "region": "US",
        }

    headers = {'Content-Type': 'application/json'}

    response = requests.post(create_session_url,
                             json=payload,
                             headers=headers,
                             params={'key': api_key})

    if response.status_code == 200:
        session_token = response.json().get('session')
        print("Session token:", session_token)
    else:
        print("Failed to create session:", response.text)

    return ("https://tile.googleapis.com/v1/2dtiles/{z}/{x}/{y}?session="
            + session_token
            + "&key="
            + api_key)

def set_tile_layout(tile_url, lat, lon, zoom=15):
    return go.Layout(
        width=640,
        height=640,
        mapbox=dict(
            style="white-bg",
            layers=[{"below": 'traces',
                     "sourcetype": "raster",
                     "sourceattribution": "Google",
                     "source": [tile_url] }],
            center=dict(lat=lat,
                        lon=lon),
            zoom=15))

if 'tiles_url' not in ss:
       ss.tiles_url = get_session_url(GOOGLE_API_KEY)

fig = go.Figure(layout=set_tile_layout(ss.tiles_url,
                                       df[lat_key].mean(),
                                       df[lon_key].mean()))

fig.add_trace(go.Scattermapbox(
          mode="markers",
          lat=df[lat_key],
          lon=df[lon_key],
          name='Data'))

fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

st.plotly_chart(fig)
