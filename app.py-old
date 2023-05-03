#! /bin/python3
# import time

# while True:
#     current_time = time.strftime("%H:%M:%S", time.localtime())
#     print(current_time)
#     time.sleep(1)


import requests
import time

while True:
    # Make curl request to OpenAPI
    response = requests.get("https://official-joke-api.appspot.com/jokes/random")
    joke = response.json()["setup"] + " " + response.json()["punchline"]
    
    # Print joke
    print(joke)
    
    # Wait for 30 seconds
    time.sleep(30)
