import requests 
base_url = "https://pokeapi.co/api/v2/"
def info(name):
    url = f"{base_url}pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Data Retrived !!")
        info = response.json()
        return info
    else:
        print(f"Error data not found error code {response.status_code}")
pokemon_name = input("Pokemon Name: ")
pokemon_info = info(pokemon_name)
print(f"Name: {pokemon_info['name'].capitalize()}")
print(f"Weight: {pokemon_info["weight"]}")
print(f"Id: {pokemon_info["id"]}")
print(f"Height:{pokemon_info["height"]}")
print("Abilities:")
for a in pokemon_info["abilities"]:
    print(f"  - {a['ability']['name']}")
    
