from django.shortcuts import render
from .api_calls import fetch_definition

def search(request):
    api_key = "3f237fea22msh646ab05d0b6341cp135065jsnff5be19a03b7"  # Replace with your actual API key
    word = "test"  # Replace with the word you want to look up
    definition = fetch_definition(word, api_key)
    print(type(definition))
    return render(request, 'dictionary/search.html', {'definition': definition})
    