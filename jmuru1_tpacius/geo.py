#get api key for google geolocation
import json
# import pymongo
import googlemaps
import apitest
import example

ticketColllectionLocations = [elem['ticket_loc'] for elem in example.ticketsCollection]
noDupes = list(set(ticketColllectionLocations))

with open('auth.json') as credentials:
	data = json.load(credentials)

# gmaps = googlemaps.Client(key=data['maps_api_key']) 
gmaps = googlemaps.Client(key=data['maps_api_key2'])

'''
make sure to create a function that appends 
(Boston, Ma) to the geolocation request.
also try and find a standard to normalize street numbers
of possible. Specifically in regards to how 
we deal with addresses with no numbers given
'''

'''
response scheme: 
geometry
place_id
formatted_address
address_components
types
'''

def generateAddr(json_obj):
	return [elem['ticket_loc'] for elem in json_obj]

def locationQueryHelper(addr):
	queryAddr = addr + ', Boston, Ma'
	geocode_result = gmaps.geocode(queryAddr)
	return ((geocode_result[0]['address_components']), str(geocode_result[0]['geometry']['location_type']))

# def locationQuery(addr_list):
# 	#extracts zip code from addresses that got tickets
# 	return [locationQueryHelper(ADDR_TICKETS[0])[0][len(locationQueryHelper(ADDR_TICKETS[0])[0])-1]['short_name'] for elem in addr_list if locationQueryHelper(elem)[1] != 'APPROXIMATE']

def locationQuery(addr_list):
	#extracts zip code from addresses that got tickets
	return [locationQueryHelper(elem[0])[0][len(locationQueryHelper(elem[0])[0])-1]['short_name'] for elem in addr_list]

def locationQueryDict(lst):
	locations = dict()
	for i in range(len(lst)):
		locations[str(i)] = lst[i]
	return locations


# zipsNoDupes = locationQuery(noDupes)

# # zips = open("zipsfromaddresses.txt", "w")
# for elem in zipsNoDupes:
# 	print(elem)
	# zips.write(elem)
# zips.close()

# print(locationQuery(noDupes)[0])
# print(locationQuery(['12 Commonwealth Ave', '870 Beacon st' ]))
# print(locationQuery(noDupes)[0])
# print(locationQuery(noDupes[0][0])[0][-2])







