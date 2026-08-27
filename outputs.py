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
Characters: {chars}""")

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
    file.write(joke_format )
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
    file.close()

def joke_doesnt_exist(joke_id, filename):
    file = open(filename,"r")
    content = file.read()
    file.close()
    if f"Joke ID: {joke_id}" not in content:
        return True


# add to main when finished
# if joke_doesnt_exist(joke_info["joke_id"],"jokeHistory.txt"):
#     add_to_history(joke_info,translation,language,"jokeHistory.txt")
# else:
#     print ("joke already exists in history")