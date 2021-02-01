import folium
from folium.map import FeatureGroup
from geopy.geocoders import ArcGIS
import webbrowser
import pandas


geo = ArcGIS()

test = pandas.read_csv("stadia.csv")
teamList = list(test['Team'])
latList = list(test['Latitude'])
longList = list(test['Longitude'])

print(test.columns)
# print(test['Latitude'])

# icon1_url = "m.png"
# icon1 = folium.features.CustomIcon(icon1_url,icon_size=(28, 30))

def group():
    sortedArr = []
    centLondon = [51.5074, 0.1277]
    #without tiles="Stamen Watercolor"
    map = folium.Map(location=centLondon, zoom_start=10)
    fg = FeatureGroup(name="FG")
    for Team in teamList:
        # print("%s : x = %s , y = %s " % (Team, latList[teamList.index(str(Team))],longList[teamList.index(str(Team))] ))
        sortedArr.append([Team, latList[teamList.index(str(Team))],longList[teamList.index(str(Team))]] )
        
        fg.add_child(folium.Marker([latList[teamList.index(str(Team))],longList[teamList.index(str(Team))]], popup=Team, icon = folium.Icon(color='pink')))
        
        print([latList[teamList.index(str(Team))],longList[teamList.index(str(Team))]])
    map.add_child(fg)
    # print(len(sortedArr))
    map.save("ftMap.html")
    webbrowser.open("ftMap.html")

group()



