import streamlit as st

@st.cache_data
def generate_image(prompt):
    client = st.session_state['openai_client']
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response.data[0].url


def update_map_state(latitude, longitude, zoom):
    """OpenAI tool to update map in-app
    """
    st.session_state[map_state] = {
        "latitude": latitude,
        "longitude": longitude,
        "zoom": zoom,
    }
    return "Map updated"

SCHEMA_GENERATE_IMAGE = {
    "type":"function",
    "function": {
        "name": "generate_image",
        "description":"Generate an image using Dall-E-3 and return the image url",
        "parameters": {
            "type":"object",
            "properties":{
                "prompt": {
                    "type":"string",
                    "description":"image generation prompt"
                }
            },
            "required":["prompt"],
            "additionalProperties": False
        },
        "strict": True
    }
}

UPDATE_MAP = {
  "name": "update_map",
  "description": "Update map to center on a particular location",
  "parameters": {
    "type": "object",
    "properties": {
      "longitude": {
        "type": "number",
        "description": "Longitude of the location to center the map on"
      },
      "latitude": {
        "type": "number",
        "description": "Latitude of the location to center the map on"
      },
      "zoom": {
        "type": "integer",
        "description": "Zoom level of the map"
      }
    },
    "required": ["longitude", "latitude", "zoom"]
  }
}
