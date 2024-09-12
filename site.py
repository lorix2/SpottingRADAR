import json
import threading

from flask import Flask, render_template
from main import Depart, Arriver, Plus_suivie
app = Flask(__name__)



@app.route("/")
def hello_world():
    depart = Depart()
    arriver = Arriver()
    list_plus_suivie = Plus_suivie()



    return render_template('index.html', flights_d=depart, flights_a=arriver, list_plus_suivie=list_plus_suivie)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)