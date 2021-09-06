import requests
dogBiteUrl = "https://data.cityofnewyork.us/resource/rsgh-akpg.json?$limit=11000"

formattedURLforJson = requests.get(f"{dogBiteUrl}")
prettyprint = formattedURLforJson.json()[1] #change the index number here.

'''this is a counter of how many times it appears in list'''

###testing function for print
def testerthing():
  print("hello!")


def appearance(phrase):
  Male = 0
  Female = 0
  Unknown = 0
  x = 10 #change value for desired range
  for i in range(x):
    prettyprint = formattedURLforJson.json()[i]
    theGender = prettyprint.get(phrase, None)
    if theGender == "M":
      Male += 1
    if theGender == "M" and i == x-1:
      Male += 1
      print(f"There are {Male} male dogs that bit people in 2015.")
      print(f"There are {Female} female dogs that bit people in 2015.")
      print(f"There are {Unknown} unidentified gender of dogs that bit people in 2015.")
    if theGender == "F":
      Female += 1
    if theGender == "F" and i == x-1:
      Female += 1
      print(f"There are {Male} male dogs that bit people in 2015.")
      print(f"There are {Female} female dogs that bit people in 2015.")
      print(f"There are {Unknown} unidentified gender of dogs that bit people in 2015.")
    if theGender == "U":
      Unknown += 1
    if theGender == "U" and i == x-1:
      Unknown += 1
      print(f"There are {Male} male dogs that bit people in 2015.")
      print(f"There are {Female} female dogs that bit people in 2015.")
      print(f"There are {Unknown} unidentified gender of dogs that bit people in 2015.")

appearance("gender")

def location(spot):
  Queens = 0
  Bronx = 0
  Brooklyn = 0
  Manhattan = 0
  Staten_Island = 0
  Other = 0
  x = 10 #change value for desired range
  for i in range(x):
    prettyprint = formattedURLforJson.json()[i]
    theSpot = prettyprint.get(spot, "Other")
    if theSpot == "Queens":
      Queens += 1
    if theSpot == "Queens" and i == x-1:
      Queens += 1
      print(Queens)
      print(Bronx)
      print(Brooklyn)
      print(Manhattan)
      print(Staten_Island)
      print(Other)
    if theSpot == "Bronx":
      Bronx += 1
    if theSpot == "Bronx" and i == x-1:
      Bronx += 1
      print(Queens)
      print(Bronx)
      print(Brooklyn)
      print(Manhattan)
      print(Staten_Island)
      print(Other)
    if theSpot == "Brooklyn":
      Brooklyn += 1
    if theSpot == "Brooklyn" and i == x-1:
      Brooklyn += 1
      print(Queens)
      print(Bronx)
      print(Brooklyn)
      print(Manhattan)
      print(Staten_Island)
      print(Other)
    if theSpot == "Manhattan":
      Manhattan += 1
    if theSpot == "Manhattan" and i == x-1:
      Manhattan += 1
      print(Queens)
      print(Bronx)
      print(Brooklyn)
      print(Manhattan)
      print(Staten_Island)
      print(Other)
    if theSpot == "Staten Island":
      Staten_Island += 1
    if theSpot == "Staten Island" and i == x-1:
      Staten_Island += 1
      print(Queens)
      print(Bronx)
      print(Brooklyn)
      print(Manhattan)
      print(Staten_Island)
      print(Other)
    if theSpot == "Other" and i == x-1:
      Unknown += 1
    if theSpot == "Other" and i == x-1:
      Unknown += 1
      print(Queens)
      print(Bronx)
      print(Brooklyn)
      print(Manhattan)
      print(Staten_Island)
      print(Other)

location("borough")


# prettyprint.get("breed", None)
