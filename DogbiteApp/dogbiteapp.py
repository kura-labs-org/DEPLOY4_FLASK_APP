from flask import Flask
import datagrabber
import sys

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World here is a basic site that lets you look at the data of dog bites related and where they occurred in NYC \n' \
           'Here you can change the top URL to "/doggender for the number of dog bites based on gender or /borough for borough location'


@app.route('/kawang')
def hello_world1():
    return 'Hello kawang'

@app.route('/doggender')
def genderdata():
    dataset = datagrabber.appearance("gender")
    print(dataset, file=sys.stderr)
    return dataset

@app.route('/testpage', methods=['GET'])
def testfunc():
    string1 = datagrabber.testerthing()
    return string1