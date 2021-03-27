import urllib.parse
import urllib.request
import json
class MapQuest:
    def __init__(self, APIkey):
        self._APIkey = APIkey
        self._baseURL = "http://open.mapquestapi.com/directions/v2/route?"
    def totalDistance(self, locations):
        if len(locations) <= 1:
            return 0
        route = [('key', self._APIkey), ('from', locations[0])]
        toLocations = locations[1:]
        for i in range(len(toLocations)):
            route.append(('to', toLocations[i]))
        fRoute = urllib.parse.urlencode(route)
        finalURL = self._baseURL + fRoute
        openURL = urllib.request.urlopen(finalURL)
        data = json.load(openURL)
        print(data)
        return data['route']['distance']


    def totalTime(self, locations):
        if len(locations) <= 1:
            return 0
        route = [('key', self._APIkey), ('from', locations[0])]
        toLocations = locations[1:]
        for i in range(len(toLocations)):
            route.append(('to', toLocations[i]))
        fRoute = urllib.parse.urlencode(route)
        finalURL = self._baseURL + fRoute
        openURL = urllib.request.urlopen(finalURL)
        data = json.load(openURL)
        print(data)
        return data['route']['time']


    def directions(self, locations):
        if len(locations) <= 1:
            return ''
        route = [('key', self._APIkey), ('from', locations[0])]
        toLocations = locations[1:]
        for i in range(len(toLocations)):
            route.append(('to', toLocations[i]))
        fRoute = urllib.parse.urlencode(route)
        finalURL = self._baseURL + fRoute
        openURL = urllib.request.urlopen(finalURL)
        data = json.load(openURL)
        print(data)
        n = ''
        for d1 in data['route']['legs']:
            for k1 in d1.keys():
                if k1 == 'maneuvers':
                    for d2 in d1[k1]:
                        for k2 in d2.keys():
                            if k2 == 'narrative':
                                n += d2[k2] + '\n'
        return n

    def pointOfInterest(self, locations, keyword, results):
        baseURL = "http://www.mapquestapi.com/geocoding/v1/address?"
        location_Parameters = [('key', self._APIkey), ('location', locations)]
        usable_location = urllib.parse.urlencode(location_Parameters)
        locationURL = baseURL + usable_location
        openURL = urllib.request.urlopen(locationURL)
        data = json.load(openURL)
        lat = 0
        lng = 0
        for d1 in data['results']:
            for k1 in d1.keys():
                if k1 == 'locations':
                    for d2 in d1[k1]:
                        for k2 in d2.keys():
                            if k2 == 'latLng':
                                for k3 in d2[k2]:
                                    if k3 == 'lat':
                                        lat = d2[k2][k3]
                                    if k3 == 'lng':
                                        lng = d2[k2][k3]
        loc = str(lng) + ',' + str(lat)
        searchBaseURL = "https://www.mapquestapi.com/search/v4/place?"
        query_parameters = [('location', loc), ('sort', 'distance'), ('key', self._APIkey), ('pageSize', results), ('q', keyword)]
        usable_search = urllib.parse.urlencode(query_parameters)
        searchURL = searchBaseURL + usable_search
        openSearchURL = urllib.request.urlopen(searchURL)
        searchData = json.load(openSearchURL)
        POI_list = []
        for d1 in searchData['results']:
            for k1 in d1.keys():
                if k1 == 'displayString':
                    POI_list.append(d1[k1])
        return POI_list

