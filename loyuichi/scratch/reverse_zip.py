#from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3
import urllib.request

#geolocator = Nominatim()
geolocator = GoogleV3()

#    location = geolocator.reverse("42.3511, -71.0603")
latlng = "42.3511,-71.0603"
location = geolocator.reverse(latlng)
#location = geolocator.reverse("52.509669, 13.376294")
print(location[0])
#print(type(location[0]))
#print(len(location[0]))
print(location[0].raw['address_components'][-1]["long_name"])
