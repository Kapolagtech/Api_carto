import config
import requests


base_url='http://api.openweathermap.org/data/2.5/weather?&appid='+config.apikey+"&units=metric"



def get_location():
    lonlat=open('C:/Users/user/Desktop/lonlatonly.txt', 'r')
    geocode=[]  #création du tableau vide
    for line in lonlat:
        lat,lon=line.split(",")  #séparation des infos dans la ligne
        coord={"lng":lon.strip(),
                "ltt": lat
                }
                # le .strip pour supprimer ('ce qui nous interesse)

        geocode.append(coord)     # fonction append qui permet d'ajouter au tableau
    return(geocode) # = voici le resultat, python nous renvoie ça


def get_weather(c):      #creation de la fonction
    lat = c['ltt']
    long = c['lng']
    url=base_url+"&lat="+lat+"&lon="+long  #cf ligne 16
    print (url)
    weather_data = requests.get(url).json()
    return(weather_data["main"])


input("Numéro de la localite :", )

coords=get_location()    #"coords" est le resultat du tableau
w=get_weather(coords[6])

print(w)


