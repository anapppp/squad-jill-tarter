from flask import Flask, render_template,url_for, request
import urllib.request,json

app = Flask(__name__)

@app.route("/")
def get_list_characters_page():

    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template("characters.html", characters = dict["results"]) 

@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data =response.read()
    dict = json.loads(data)
    
    return render_template("profile.html", profile=dict)

@app.route("/lista")
def get_list_characters():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters= response.read()
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