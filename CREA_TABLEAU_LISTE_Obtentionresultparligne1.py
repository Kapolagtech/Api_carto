# coord1 = {'lat':45.766504,'lon':5.791166}
# coord2 = {'lat':45.764019,'lon':5.788881}
# coord3 = {'lat':45.759428,'lon':5.790793}
# coord4 = {'lat':45.762664,'lon':5.792797}
# coord5 = {'lat':45.762664,'lon':5.792797}
# coord6 = {'lat':45.754700,'lon':5.787025}
# coord7 = {'lat':45.753517,'lon':5.789181}
# coord8 = {'lat':45.751544,'lon':5.794889}
# coord9 = {'lat':45.750691,'lon':5.792722}
# coord10 = {'lat':45.751511,'lon':5.796375}
# coord11 = {'lat':45.750111,'lon':5.793934}
import requests

#geocode=[coord1,coord2,coord3,coord4,coord5,coord6,coord7coord8,coord9,coord10,coord11]
#print(geocode[0])
#print(geogode[1])
api='&appid=65cac0f456f55747c7f58e9ba1e824d0'
base_url='http://api.openweathermap.org/data/2.5/weather?'+api+"&units=metric"

# tout ca c'est sympa mais autant le sortir du fichier :


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
    print(geocode)
    return(geocode) # = voici le resultat, python nous renvoie ça


def get_weather(c):      #creation de la fonction
    lat = c['ltt']
    long = c['lng']
    url=base_url+"&lat="+lat+"&lon="+long  #cf ligne 16
    print (url)
    weather_data = requests.get(url).json()
    return(weather_data["main"])

coords=get_location()    #"coords" est le resultat du tableau
print(coords[5]);
w=get_weather(coords[6])

print(w)


