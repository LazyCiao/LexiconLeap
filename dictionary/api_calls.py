import requests
import json

def fetch_definition(word, api_key):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}"
    headers = {
        "X-Mashape-Key": api_key,
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        data = response.json()
        form_data = json.dumps(data, indent=1)
        # print(form_data)

        # Processing the response data


        # results = data.get("results", [])
        # print(results['definition'])


        # syllables = data.get("syllables", {})
        # pronunciation = data.get("pronunciation", {}).get("all", "")

        # word_details = {
        #     "definitions": [result.get("definition", "") for result in results],
        #     "partOfSpeech": [result.get("partOfSpeech", "") for result in results],
        #     "synonyms": [result.get("synonyms", []) for result in results],
        #     "typeOf": [result.get("typeOf", []) for result in results],
        #     "derivation": [result.get("derivation", []) for result in results],
        #     "syllable_count": syllables.get("count", 0),
        #     "syllable_list": syllables.get("list", []),
        #     "pronunciation": pronunciation
        # }

        return data

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None