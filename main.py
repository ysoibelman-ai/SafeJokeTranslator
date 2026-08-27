import json
import csv
from requests import get
import questionary


def get_language():
    language = questionary.select("please choose a language:", choices = ["Hebrew","Spanish","French","Italian"]).ask()
    match language:
        case "Hebrew":
            language = "hb"
        case "Spanish":
            language = "es"
        case "French":
            language = "fr"
        case "Italian":
            language = "it"
    return language



def get_joke():
    url = "https://v2.jokeapi.dev/joke/Programming?type=single&blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
    params = {}
    joke = get(url).json()
    print (joke)
    return joke

def is_safe_joke(joke_data):
    jk = joke_data
    if jk['error'] == False and jk["type"] == "single" and jk["joke"] != "" and jk["flags"]["nsfw"] == False and jk["flags"]["religious"] == False and jk["flags"]["political"] == False and jk["flags"]["racist"] == False and jk["flags"]["nsfw"] == False and jk["flags"]["sexist"] == False and jk["flags"]["explicit"] == False:
        return True
    return False

def get_safe_joke():
    for _ in range (3):
        joke = get_joke()
        if is_safe_joke(joke):
            return joke
    return None

def extract_joke_data(api_data):
    joke_info ={}
    joke_info["joke"] = api_data["joke"]
    joke_info["category"] = api_data["category"]
    joke_info["joke_id"] = api_data["id"]
    joke_info["language"] = api_data["language"]

    return joke_info

def analyze_joke(joke):
    joke_text = joke["joke"]
    characters = len(joke_text)
    words = len(joke_text.split())
    joke_analysis = {"joke":joke_text,"Characters":characters,"Words":words}
    return joke_analysis

def translate_joke(joke,target_laguange):
    url = "https://translated.net"
    params_ = {"q": joke,"langpair": f"en|{target_laguange}"}  
    translation = get(url, params=params_)
    return translation


print (translate_joke("Hello","hb"))



    
