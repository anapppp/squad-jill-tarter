from flask import Flask, render_template, url_for 
import urllib.request
import json


app = Flask(__name__)


@app.route("/characters/<int:page>")
def get_list_characters_page(page=1):
    url = f"https://rickandmortyapi.com/api/character/?page={page}"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template("characters.html", characters=dict["results"], page=page)


@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template("profile.html", profile=dict)


@app.route("/locations/<int:page>")    #PAULA PRECISA TERMINAR
def get_locations_page(page=1):
    url = f"https://rickandmortyapi.com/api/location/?page={page}"
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
    return render_template("locations.html", locations=locations_list, page=page)


@app.route("/location/<id>")
def get_location(id):
    url = "https://rickandmortyapi.com/api/location/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template("location.html", location=dict)


@app.route("/episodes/<int:page>")
def get_episodes_page(page=1, total_pages=None):  
    url = f"https://rickandmortyapi.com/api/episode/?page={page}&total_pages=3"
    try:
        response = urllib.request.urlopen(url)
        episodes_data = response.read()
        dict = json.loads(episodes_data)
    
        if "info" in dict and "pages" in dict["info"]:
            total_pages = dict["info"]["pages"]

    except Exception as e:
        print(f"Error fetching episode data: {e}") 
        return render_template("error.html")

    return render_template("episodes.html", episodes_list=dict.get("results", []), page=page, total_pages=total_pages)

@app.route("/episode/<id>")
def get_episode(id):
    url = "https://rickandmortyapi.com/api/episode/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template("episode.html", episode=dict)

@app.route("/")
def home():
    return get_list_characters_page()

if __name__ == "__main__":
     app.run(debug=False)