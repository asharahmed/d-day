import folium
from folium.plugins import PolyLineTextPath

# create map centered on beach landing
map_center = (49.372, -0.905)
my_map = folium.Map(location=map_center, zoom_start=10)

# add markers for beach landing locations
beach_landing_locations = {
    "Omaha Beach": {"location": [49.372, -0.905], "country": "USA"},
    "Gold Beach": {"location": [49.342, -0.607], "country": "UK"},
    "Juno Beach": {"location": [49.365, -0.562], "country": "Canada"},
    "Sword Beach": {"location": [49.325, -0.283], "country": "UK"},
    "Utah Beach": {"location": [49.409, -1.247], "country": "USA"},
    "Vierville-sur-Mer": {"location": [49.3711, -0.851], "country": "USA"},
    "Colleville-sur-Mer": {"location": [49.3472, -0.8572], "country": "USA"},
    "Bayeux": {"location": [49.2769, -0.7039], "country": "UK"},
    "Caen": {"location": [49.1828, -0.3709], "country": "UK"},
    "Courseulles-sur-Mer": {"location": [49.3333, -0.45], "country": "Canada"},
    "Pegasus Bridge": {"location": [49.2531, -0.2694], "country": "UK"},
    "Sainte-Mère-Église": {"location": [49.4053, -1.3078], "country": "USA"},
    "Carentan": {"location": [49.3039, -1.2422], "country": "USA"},
    "Saint-Laurent-sur-Mer": {"location": [49.3611, -0.8833], "country": "USA"},
    "Arromanches-les-Bains": {"location": [49.3531, -0.5], "country": "UK"},
    "Sainte-Marie-du-Mont": {"location": [49.4167, -1.2833], "country": "USA"},
    "Bernières-sur-Mer": {"location": [49.3667, -0.5333], "country": "Canada"},
    "Hermanville-sur-Mer": {"location": [49.3167, -0.2167], "country": "UK"},
    "Formigny": {"location": [49.3667, -0.9333], "country": "USA"}

}
for beach, loc in beach_landing_locations.items():
    # add marker for beach landing location
    # color code markers by country
    country = beach_landing_locations[beach]["country"]
    color = 'red' if country == "USA" else 'green' if country == "UK" else 'blue' if country == "Canada" else 'gray'


    folium.Marker(location=loc["location"], popup=beach, icon=folium.Icon(color=color)).add_to(my_map)

# add arrows for troop movements
troop_movements = [
    ("Omaha Beach", "Vierville-sur-Mer", 5000),
    ("Omaha Beach", "Colleville-sur-Mer", 3500),
    ("Omaha Beach", "Saint-Laurent-sur-Mer", 2500),
    ("Omaha Beach", "Formigny", 4000),
    ("Utah Beach", "Sainte-Marie-du-Mont", 3000),
    ("Utah Beach", "Sainte-Mère-Église", 2000),
    ("Gold Beach", "Bayeux", 3500),
    ("Gold Beach", "Arromanches-les-Bains", 2000),
    ("Juno Beach", "Courseulles-sur-Mer", 3000),
    ("Juno Beach", "Bernières-sur-Mer", 2500),
    ("Sword Beach", "Hermanville-sur-Mer", 1500),
    ("Sword Beach", "Caen", 2500)
]

for start_beach, end_beach, troop_count in troop_movements:
    start_loc = beach_landing_locations[start_beach]
    end_loc = beach_landing_locations[end_beach]

    # get country of start beach
    start_beach_country = None
    for beach, loc in beach_landing_locations.items():
        if beach == start_beach:
            start_beach_country = loc['country']
            break

    # set color of arrow based on start beach country
    color = 'red' if start_beach_country == "USA" else 'green' if start_beach_country == "UK" else 'blue' if start_beach_country == "Canada" else 'gray'

    folium.PolyLine(locations=[start_loc["location"], end_loc["location"]],
                    weight=troop_count/1000,
                    color=color,
                    opacity=1,
                    tooltip=f"{troop_count} troops").add_to(my_map)



my_map.save('map_with_arrows.html')
