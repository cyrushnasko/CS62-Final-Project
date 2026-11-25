"""Download the Spring 2027 course data from Hyperschedule and save it to data/SP2027.json.

The data has one entry per section of each course.
"""

import json
import os
import urllib.request

URL = "https://banana.hyperschedule.io/v4/sections/SP2027"

# Hyperschedule refuses requests that don't name the program making them,
# so we give ours a name.
request = urllib.request.Request(URL, headers={"User-Agent": "cs62-course-graph"})
response = urllib.request.urlopen(request)
sections = json.load(response)

os.makedirs("data", exist_ok=True)
with open("data/SP2027.json", "w") as f:
    json.dump(sections, f, indent=1)

print("Saved", len(sections), "sections to data/SP2027.json")