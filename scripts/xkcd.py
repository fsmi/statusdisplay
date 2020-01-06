#!/usr/bin/env python3

import time
import subprocess
import json
import requests
import random
import urllib.request
import types
import argparse

def getMaxIteration():
	response = requests.get("https://xkcd.com/info.0.json")
	newestXkcd = json.loads(response.text)
	return newestXkcd['num']

# parsing waittime
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--time", help="the time in seconds an image will be shown", type=int)
args = parser.parse_args()
if args.time:
	waittime = args.time
	print("waittime: " + str(waittime))
else:
	waittime = 30

# pathvarioable for temporary image location
path = "/tmp/xkcd.png"

# startvalue
maxIteration = getMaxIteration()
i = random.randint(1, maxIteration)
processDisplay = 0

while True:
	while i <= maxIteration:
		response = requests.get("https://xkcd.com/" + str(i) + "/info.0.json")
		newestXkcd = json.loads(response.text)
		imageUrl = newestXkcd['img']
		# download image and save it in /tmp/
		with urllib.request.urlopen(imageUrl) as response, open(path, 'wb') as outFile:
			data = response.read() # a `bytes` object
			outFile.write(data)
		
		# convert image
		subprocess.call("convert " + path + " +profile 'icc' -fuzz 60% -fill '#00FF00' -opaque black " + path, shell=True)
		subprocess.call("convert " + path + " +profile 'icc' -fuzz 40% -fill black -opaque white " + path, shell=True)
		
		# display converted image
		if isinstance(processDisplay, subprocess.Popen):
			processDisplay.kill()
		processDisplay = subprocess.Popen(['feh', "-s", "-Z", "--image-bg", "black", path])
		
		# wait
		time.sleep(waittime)
		i+=1
	maxIteration = getMaxIteration()
	i = 0
