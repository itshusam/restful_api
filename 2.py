import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('englishName', 'N/A')
            mass = mass = planet['mass']['massValue'] * 10 ** planet['mass']['massExponent'] if 'mass' in planet else 'N/A'
            orbit_period = planet.get('sideralOrbit', 'N/A')
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()