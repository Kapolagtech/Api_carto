import smopy
import requests
from IPython.display import Image
import matplotlib.pyplot as plt

APIK="65cac0f456f55747c7f58e9ba1e824d0"

#​https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&
#exclude={part}&appid={YOUR API KEY}


complete_url = "https://api.openweathermap.org/data/2.5/onecall" + "?lat=" + lattitude + "&lon=" + longitude + "&appid=" + APIK

parcelles = ["sonjon","monette","ressoniere","patavine","longefan","blanchettes","combes","eglise","altesses","mollard","pimpenan","sarasin","thomasettes"]
#longefan = 45.759428, 5.790793

first=True

def coordonnees(parcelles, lattitude, longitude):
        lattitude = 5.790793
        longitude = 45.759428
def parcelles (coordonnees, complete_url)

for nom_parcelle in parcelles :
    complete_url = "https://api.openweathermap.org/data/2.5/onecall" + "?lat=" + lattitude + "&lon=" + longitude + "&appid=" + APIK +"&units=metric"
#http://api.openweathermap.org/data/2.5/weather?lat=5.790793&lon=45.759428&units=imperial&appid=65cac0f456f55747c7f58e9ba1e824d0 pour longefan


weather_data = requests.get(complete_url).json()

print(weather_data)

posx=(weather_data['coord']['lon'])
posy=(weather_data['coord']['lat'])




if first:
    map = smopy.Map((posy-1, posx-1, posy+1, posx+1),z=8)

    first=False
    ax=map.show_mpl(figsize=(4,4))

    x,y=map.to_pixels(posy,posx)

    ax.plot(x,y,"or",ms=5,mew=2)

    ax.annotate(weather_data['main']['temp'],xy=(x,y),xytext=(3,3),textcoords="offset points")
    plt.show()

    map.save_png('/home/asthro/Projets/50-Pop/pyt/map.png')
