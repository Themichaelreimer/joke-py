from random import choice
import requests

JOKE_SOURCES = [
    {"url": "https://icanhazdadjoke.com/", "headers": {"accept": "application/json"}, "get_joke": lambda o: o["joke"]},
    {"url": "https://api.chucknorris.io/jokes/random", "headers": {}, "get_joke": lambda o: o["value"]},
    {"url": "https://v2.jokeapi.dev/joke/Any", "headers": {}, "get_joke": lambda o: o["joke"] if "joke" in o else f"{o["setup"]}\n{o["delivery"]}" },
]

def random_joke() -> str:
    source = choice(JOKE_SOURCES)
    response = requests.get(source["url"], headers=source["headers"])
    if response.status_code == 200:
        return source["get_joke"](response.json())
    else:
        print(response.text)

if __name__ == "__main__":
    print(random_joke())