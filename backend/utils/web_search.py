import requests

def smart_search(query):
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    response = requests.get(url).json()
    if response.get("AbstractText"):
        return response["AbstractText"]
    return "No answer found."
