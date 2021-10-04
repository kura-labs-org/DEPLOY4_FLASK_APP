from flask import Flask
import datagrabber

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World here is a basic site that lets you look at the data of dog bites related and where they occurred in NYC \n' \
           'Here you can change the top URL to "/doggender for the number of dog bites based on gender or /borough for borough location'


@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name}'

@app.route('/gender/<command>')
def genderdata(command):
    dataset = datagrabber.appearance(f"{command}")
    return datagrabber.appearance(f"{command}")

@app.route('/borough')
def locationdata():
    dataset = datagrabber.location("borough")
    return datagrabber.location("borough")


@app.route('/testpage', methods=['GET'])
def testfunc():
    string1 = datagrabber.testerthing()
    return string1