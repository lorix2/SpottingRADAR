import json


from FlightRadar24 import FlightRadar24API
fr_api = FlightRadar24API()

def Depart():
    airport = fr_api.get_airport_details("ELLX")
    list_depart = {}

    i = 0
    depart = airport["airport"]["pluginData"]["schedule"]["departures"]["data"]
    for flight in depart[:5]:
        list_depart[i] ={}
        list_depart[i]["registration"] = flight["flight"]["aircraft"]["registration"]
        list_depart[i]["aircraft"] = flight["flight"]["aircraft"]["model"]["text"]
        list_depart[i]["time"] = flight['flight']['status']['text']
        i +=1

    with open("sample2.json", "w") as outfile:
        json.dump(airport, outfile)
    return list_depart


def Arriver():
    airport = fr_api.get_airport_details("ELLX")
    list_arriver = {}

    i = 0
    arriver = airport["airport"]["pluginData"]["schedule"]["arrivals"]["data"]
    for flight in arriver[:5]:
        list_arriver[i] = {}
        list_arriver[i]["registration"] = flight["flight"]["aircraft"]["registration"]
        list_arriver[i]["aircraft"] = flight["flight"]["aircraft"]["model"]["text"]
        list_arriver[i]["time"] = flight['flight']['status']['text']
        i += 1

    return list_arriver

def Plus_suivie():
    i = 0
    n = fr_api.get_most_tracked()

    list_plus_suivie = {}
    for flight in n["data"]:
        list_plus_suivie[i] = {}
        list_plus_suivie[i]["model"] = flight["type"]
        list_plus_suivie[i]["registration"] = flight["callsign"]
        i += 1
    return list_plus_suivie






