import requests
def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    
    try:
        response = requests.get(url,timeout=5)
        response.raise_for_status()
        data = response.json()
        print(f"name: {data["name"]}")  
        print(f"pokemon id:{data["id"]}")      
        print(f"height of {name} : {data["height"]}")   
        print(f"weight of {name} : {data["weight"]}")   
        print("ability :-")
        for item in data["abilities"]:
            print(item["ability"]["name"])
        return name
    except requests.exceptions.HTTPError:
        print("name not found , check the name again")
    except requests.exceptions.ConnectionError: 
        print("No internet connection.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again.")
    except requests.exceptions.RequestsJSONDecodeError:
        print(f"couldnt read data for {name} try again")
name_pokemon = input("Pokemon's name: ")
get_pokemon(name_pokemon)