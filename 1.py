import requests
import json


response=requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
json_data=response.text


pikatchu=json.loads(json_data)


print(pikatchu["name"])
print(pikatchu["abilities"])




#2
def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get data for {pokemon_name}")
        return None
    

def calculate_average_weight(pokemon_list):
    total_weight = 0
    count = 0
    for pokemon in pokemon_list:
        if pokemon:
            total_weight += pokemon['weight']
            count += 1
    return total_weight / count if count > 0 else 0


def print_pokemon_info(pokemon_data):
    name = pokemon_data['name'].capitalize()
    abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
    weight = pokemon_data['weight']
    print(f"Name: {name}")
    print("Abilities:", ", ".join(abilities))
    print(f"Weight: {weight}")



pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_data_list = []


for name in pokemon_names:
        data = fetch_pokemon_data(name)
        if data:
            pokemon_data_list.append(data)
            print_pokemon_info(data)
            print()

average_weight = calculate_average_weight(pokemon_data_list)
print(f"Average Weight of {', '.join([name.capitalize() for name in pokemon_names])}: {average_weight}")
