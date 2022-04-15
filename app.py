import json
from flask import Flask, request, render_template
from requests.auth import HTTPBasicAuth
import requests

app = Flask(__name__)
# My auth key. Necessary for api request: CnJUSLjs9yT3mMjZZSHkSyt0ZjwgrFHqqPA0bp5C.
# New auth keys can be obtained by making an account on ballchasing.com.

# Landing page for app. Contains routes to view other features. 
@app.route("/")
def start():
    return render_template("start.html")

if __name__ == '__main__':
    app.run(debug= True, port=5000)

# Route to view replays
@app.route("/replays")
def response1():
    response = requests.get('https://ballchasing.com/api/replays/', 
    headers = {'Authorization':'CnJUSLjs9yT3mMjZZSHkSyt0ZjwgrFHqqPA0bp5C'})
    data = response.json()
    return render_template("replays.html", data=data)

# Route to view a pro replay
@app.route('/request_pro')
def response2():
    response = requests.get('https://ballchasing.com/api/replays/?pro=true', 
    headers = {'Authorization':'CnJUSLjs9yT3mMjZZSHkSyt0ZjwgrFHqqPA0bp5C'})
    data = response.json()
    return render_template("pro_replays.html", data=data)
    
# Renders HTML for player search
@app.route('/player_search')
def response3():
    return render_template('player_search.html')

# Submit player search
@app.route('/search_submit', methods =["GET", "POST"])
def response4():
    if request.method =="POST":
        param = request.form.get("name")
    response = requests.get('https://ballchasing.com/api/replays/?player-name='+param,
    headers = {'Authorization':'CnJUSLjs9yT3mMjZZSHkSyt0ZjwgrFHqqPA0bp5C'})
    data = response.json()
    return render_template("search_submit.html", data=data)