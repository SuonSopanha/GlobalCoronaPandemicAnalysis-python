import folium

# Create a base map
map = folium.Map(location=[37.25, 127.05], zoom_start=12)

# Save the base map to a file
map.save('map.html')

# Create a marker map
marker_map = folium.Map(location=[45.372, -121.6972], zoom_start=13)

# Add markers to the marker map
folium.Marker(
    location=[45.3288, -121.6625],
    popup='Mt. Hood Meadows',
    icon=folium.Icon(icon='cloud'),
).add_to(marker_map)

folium.Marker(
    location=[45.3311, -121.7113],
    popup='Timberline Lodge',
    icon=folium.Icon(color='green'),
).add_to(marker_map)

# Add a circle marker to the marker map
folium.CircleMarker(
    location=[45.3300, -121.6823],
    radius=100,  # Corrected typo: "raduis" to "radius"
    popup='circle',
    color='blue',
    fill=True,
    fill_color='red',
).add_to(marker_map)

# Save the marker map to a file
marker_map.save('map2.html')
