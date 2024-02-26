from flask import Flask, render_template, url_for, request
import urllib.request
import json


app = Flask(__name__)


@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template("characters.html", characters=dict["results"])


@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template("profile.html", profile=dict)


@app.route("/lista")
def get_list_characters():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    characters_list = []
    for character in dict["results"]:
        character_dict = {
            "Nome": character["name"],
            "Espécie": character["species"],
            "Gênero": character["gender"],
            "Origem": character["origin"]["name"],
            "Localização": character["location"]["name"],
        }
        characters_list.append(character_dict)
    return {"characters": characters_list}


@app.route("/locations")   # PAULA PRECISA TERMINAR
def get_locations():
    url = "https://rickandmortyapi.com/api/location/"
    response = urllib.request.urlopen(url)
    location_data = response.read()
    locations_dict = json.loads(location_data)

    locations_list = []
    for location in locations_dict["results"]:
        location_dict = {
            "name": location["name"],
            "type": location["type"],
            "dimension": location["dimension"],
            "id": location["id"]
        }
        locations_list.append(location_dict)
    return render_template("locations.html", locations=locations_list)


@app.route("/locations/<id>")  # MAISA DEVE COMPLETAR
def get_location(id):
    url = "https://rickandmortyapi.com/api/location/" + id
    return url

@app.route("/episodes") #SARAH
def get_list_espisodes():
    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url)
    episodes_data = response.read()    
    dict = json.loads(episodes_data)
        
    espisodes_list = []
    for episode in dict["results"]:
            episodes_info = {
                "Nome": episode["name"],
                "Data de Lançamento": episode["air_date"],
                "Codigo": episode["id"],
                "Episódio": episode["episode"],
                }
            espisodes_list.append(episodes_info)
        
    return {"episodes": espisodes_list}

@app.route("/episodios")
def get_list_episodes_page():
    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("episodes.html", episodes_list=dict["results"])


@app.route("/episodes/<id>")  # ANA PAULA DEVE COMPLETAR
def get_episode(id):
    url = "https://rickandmortyapi.com/api/episode/" + id
    return url
