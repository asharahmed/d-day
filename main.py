import folium
from folium.plugins import AntPath

# create a map centered at Normandy
map_center = (49.372, -0.905)
m = folium.Map(location=map_center, zoom_start=10)

# define the beach landing locations
beach_locations = {
    "Omaha Beach": {"location": [49.372, -0.905], "country": "USA"},
    "Gold Beach": {"location": [49.342, -0.607], "country": "UK"},
    "Juno Beach": {"location": [49.365, -0.562], "country": "Canada"},
    "Sword Beach": {"location": [49.325, -0.283], "country": "UK"},
    "Utah Beach": {"location": [49.409, -1.247], "country": "USA"},
    "Vierville": {"location": [49.3711, -0.851], "country": "USA"},
    "Colleville": {"location": [49.3472, -0.8572], "country": "USA"},
    "Bayeux": {"location": [49.2769, -0.7039], "country": "UK"},
    "Caen": {"location": [49.1828, -0.3709], "country": "UK"},
    "Courseulles": {"location": [49.3333, -0.45], "country": "Canada"},
    "Pegasus Bridge": {"location": [49.2531, -0.2694], "country": "UK"},
    "Sainte-Mère-Église": {"location": [49.4053, -1.3078], "country": "USA"},
    "Carentan": {"location": [49.3039, -1.2422], "country": "USA"}
}

# define the troop movements
troop_movements = [
    {"start": "Omaha Beach", "end": "Vierville", "country": "USA"},
    {"start": "Omaha Beach", "end": "Colleville", "country": "USA"},
    {"start": "Gold Beach", "end": "Bayeux", "country": "UK"},
    {"start": "Gold Beach", "end": "Caen", "country": "UK"},
    {"start": "Juno Beach", "end": "Courseulles", "country": "Canada"},
    {"start": "Sword Beach", "end": "Pegasus Bridge", "country": "UK"},
    {"start": "Utah Beach", "end": "Sainte-Mère-Église", "country": "USA"},
    {"start": "Utah Beach", "end": "Carentan", "country": "USA"}
]

# add markers to the map for each beach location
for name, data in beach_locations.items():
    folium.Marker(
        location=data["location"],
        popup=name,
        icon=folium.Icon(color='red' if data["country"] == "USA" else 'green' if data["country"] == "UK" else 'blue' if data["country"] == "Canada" else 'gray')
    ).add_to(m)

# add arrows to the map for each troop movement
for movement in troop_movements:
    start_location = beach_locations[movement["start"]]["location"]
    end_location = beach_locations[movement["end"]]["location"]
    color = 'red' if movement["country"] == "USA" else 'green' if movement["country"] == "UK" else 'blue' if movement["country"] == "Canada" else 'gray'
    
    folium.PolyLine(
    locations=[start_location, end_location],
    color=color,
    weight=5,
    opacity=1,
    arrowhead_scale=1,
    tooltip=movement["country"],
    dash_array='10,5',
    show=True
).add_to(m)
    


# save the map as an HTML file and open it in a web browser
m.save("troop_movements.html")
