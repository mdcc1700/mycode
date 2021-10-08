#!/usr/bin/env python3
import urllib.request
import json

# Call the API Nasa
apodurlobj=urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=17wr3adrJmIztZcQ5BkCNdhDprdpjQTFLY5LNUTF")

# Read APOD (Astronomy Picture of the Day) Object
apodread=apodurlobj.read()

# Decode jsont to Python Data Structure
decodeapod=json.loads(apodread.decode('utf-8'))

# Display Pythonic Data
# print(decodeapod)
print ("Copyright: ",decodeapod['copyright'])
print ("Date: ",decodeapod['date'])
print ("Explanation: ",decodeapod['explanation'])
print ("HDURL Image: ",decodeapod['hdurl'])
print ("Media Type: ",decodeapod['media_type'])
print ("Service Version: ",decodeapod['service_version'])
print ("Title: ",decodeapod['title'])
print ("URL",decodeapod['url'])
