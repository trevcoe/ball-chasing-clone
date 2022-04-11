import json
from flask import Flask, request, render_template
from requests.auth import HTTPBasicAuth
import requests

app = Flask(__name__)
# My auth key. Necessary for api request: CnJUSLjs9yT3mMjZZSHkSyt0ZjwgrFHqqPA0bp5C

# Landing page for app. Contains routes to view other features. 
@app.route("/")
def start():
    return render_template("start.html")

if __name__ == '__main__':
    app.run(debug= True, port=5000)

# Route to view replays
@app.route("/replays")
def response1():
    response = requests.get('https://ballchasing.com/api/replays',
    headers = {'Authorization':'CnJUSLjs9yT3mMjZZSHkSyt0ZjwgrFHqqPA0bp5C'})
   
    # convert data to dict
    data = json.loads(response.text)

    # Convert dict to string
    data = json.dumps(data)
    return data

# Route to view a pro replay
@app.route('/request_pro')
def response2():
    response = requests.get('https://ballchasing.com/api/replays/?pro=true', 
    headers = {'Authorization':'CnJUSLjs9yT3mMjZZSHkSyt0ZjwgrFHqqPA0bp5C'})
    return response.json()
    
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
    return response.json()