from outputs import print_out,save_joke,add_to_history,joke_doesnt_exist
from joke import get_language,get_safe_joke,extract_joke_data,analyze_joke,translate_joke

def main ():
    for _ in range (3):
        language = get_language()
        joke_json = get_safe_joke()
        if joke_json:
            joke_info = extract_joke_data(joke_json)
            joke_analysis = analyze_joke(joke_info)
            translation = translate_joke(joke_info["joke"],language)
            save_joke(joke_info,joke_analysis,translation,language,"currentJoke.txt")
            print_out(joke_info["joke"],translation,joke_info["category"],joke_analysis["Words"],joke_analysis["Characters"])
main ()