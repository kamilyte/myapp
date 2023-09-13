from django.shortcuts import render
from django.http import HttpResponse
from serpapi import GoogleSearch

# Create your views here.
def index(request):
    context = {
        'name' : 'World'
    }

    return render(request, 'index.html', context)

def printCSV(request):
    print("Title,Authors,Year,Citations\n")

def themisInput(request):
    search = input()
    name = input()
    selfCitations = input()

def googleSearch(request):

    # get author ID from Google Scholar API
    params = {
        "engine" : "google_scholar",
        "q" : "Arnold Meijster",
        "api_key" : "c1b57a5186ae96e31b5966c89200e8fbe3491fb9854ad5089f56feed874dcf57"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    organic_results = (results["organic_results"])[0]
    print(organic_results)
    return HttpResponse(organic_results)



