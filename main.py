import json
import csv
import deepl
from requests import get
import questionary


def get_language():
    language = questionary.select("please choose a language:", choices = ["Hebrew","Spanish","French","Italian"]).ask()
    match language:
        case "Hebrew":
            language = "HE"
        case "Spanish":
            language = "ES"
        case "French":
            language = "FR"
        case "Italian":
            language = "IT"
    return language

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Programming?type=single&blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
    joke = get(url).json()
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
    joke_info["language"] = api_data["lang"]

    return joke_info

def analyze_joke(joke):
    joke_text = joke["joke"]
    characters = len(joke_text)
    words = len(joke_text.split())
    joke_analysis = {"joke":joke_text,"Characters":characters,"Words":words}
    return joke_analysis

def translate_joke(joke,target_laguange):
    auth_key = "3269b51f-770a-40b6-99b1-204f919ac290:fx"
    deepl_client = deepl.DeepLClient(auth_key)
    try:
        result = deepl_client.translate_text(joke, target_lang=target_laguange)
        return result
    except:
        print ("No translation")

def print_out(joke,translation,category,words,chars):
    print(f"""

SAFE PROGRAMMING JOKE
=====================
Original:
{joke}

Translation:
{translation}

Information:
Category: {category}
Words: {words}
Characters: {chars}

            """)

def save_joke(joke_data, analysis, translated_joke, language, filename):
    joke_format =f"""
SAFE JOKE
=========

Category: {joke_data["category"]}
Joke ID: {joke_data["joke_id"]}

Original:
{joke_data["joke"]}

Translation language:
{language}

Translation:
{translated_joke}

Words: {analysis["Words"]}
Characters: {analysis["Characters"]}"""

    file = open(filename,"w",encoding="utf-8")
    file.write(joke_format)
    file.close()

def add_to_history(joke_data, translated_joke, language, filename):
    file = open (filename,"a+",encoding="utf-8")
    joke_format = f"""
------------------------------
Joke ID: {joke_data["joke_id"]}
Language: {language}

Original:
{joke_data["joke"]}

Translation:
{translated_joke}
"""
    file.write(joke_format)


def joke_doesnt_exist(joke_id, filename):
    file = open(filename,"r")
    content = file.read()
    file.close()
    if f"Joke ID: {joke_id}" not in content:
        return True

def main ():

    for _ in range (3):
        language = get_language()
        joke_json = get_safe_joke()
        if joke_json:
            joke_info = extract_joke_data(joke_json)
            joke_analysis = analyze_joke(joke_info)
            translation = translate_joke(joke_info["joke"],language)
            save_joke(joke_info,joke_analysis,translation,language,"currentJoke.txt")
            if joke_doesnt_exist(joke_info["joke_id"],"jokeHistory.txt"):
                add_to_history(joke_info,translation,language,"jokeHistory.txt")
            else:
                print ("joke already exists in history")


    # print_out(joke_info["joke"],translation,joke_info["category"],joke_analysis["Words"],joke_analysis["Characters"])

main ()





    
