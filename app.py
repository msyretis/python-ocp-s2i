import subprocess
import requests
import time

# Create a virtual environment and activate it
subprocess.run(["python3", "-m", "venv", "myenv"])
subprocess.run(["source", "myenv/bin/activate"])

# Install dependencies in the virtual environment
subprocess.run(["pip", "install", "requests"])

while True:
    # Make curl request to OpenAPI
    response = requests.get("https://official-joke-api.appspot.com/jokes/random")
    joke = response.json()["setup"] + " " + response.json()["punchline"]
    
    # Print joke
    print(joke)
    
    # Wait for 30 seconds
    time.sleep(30)