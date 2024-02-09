import folium
import json

from step1 import total_df
center = [37.26, 84.08]


m = folium.Map(
    location=center,
    zoom_start=2,
    max_bounds=True,
    min_zoom=1,
    min_lat=-84,
    max_lat=84,
    min_lon=-175,
    max_lon=187,)

geo_path = "World_Countries_Generalized.geojson"

json_data = json.load(open(geo_path))

folium.Choropleth(geo_data=json_data,data=total_df,columns=(total_df.index,'total_vaccinations_per_hundred'),key_on='properties.COUNTRY',fill_color='YlOrRd',fill_opacity=0.7,line_opacity=0.5).add_to(m)

m.save("map4.html")