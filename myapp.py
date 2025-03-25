import requests
import json

# Current version of the application
CURRENT_VERSION = "1.0"

# URL to the latest version JSON file (to be hosted on GitHub)
VERSION_URL = "https://raw.githubusercontent.com/yourusername/yourrepo/main/latest_version.json"

def check_for_updates():
    try:
        response = requests.get(VERSION_URL)
        response.raise_for_status()  # Raise an error if the request fails
        latest_info = json.loads(response.text)
        latest_version = latest_info["version"]
        download_url = latest_info["download_url"]
        
        if latest_version > CURRENT_VERSION:
            print(f"A new version ({latest_version}) is available! Download it from: {download_url}")
        else:
            print("You are using the latest version.")
    except requests.exceptions.RequestException:
        print("Unable to check for updates. Please check your internet connection.")

def main():
    print("Welcome to MyApp Version", CURRENT_VERSION)
    check_for_updates()
    
    # Simple program: add two numbers
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = a + b
    print(f"The sum of {a} and {b} is {result}")

if __name__ == "__main__":
    main()