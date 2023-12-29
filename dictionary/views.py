from django.shortcuts import render
from .api_calls import fetch_definition

def search(request):
    api_key = ""  # Replace with your actual API key
    word = "test"  # Replace with the word you want to look up
    definition = fetch_definition(word, api_key)
    print(type(definition))
    return render(request, 'dictionary/search.html', {'definition': definition})
    
