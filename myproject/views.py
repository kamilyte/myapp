from django.shortcuts import render
from django.http import HttpResponse
from serpapi import GoogleSearch

# Create your views here.

# dummy function
def index(request):
    context = {
        'name' : 'World'
    }

    return render(request, 'index.html', context)


def themisInput(request):
    search = input()
    name = input()
    selfCitations = input()

def googleSearch(request):

    # get author ID from Google Scholar API
    name = "Arnold Meijster"  # !!!!! replace with query parameter !!!!!
    split_name = name.split()
    first_letter = split_name[0][0]
    surname = split_name[1]
    author_name = first_letter + " " + surname
    params = {
        "engine" : "google_scholar",
        "q" : "author: " + name,
        "api_key" : "c1b57a5186ae96e31b5966c89200e8fbe3491fb9854ad5089f56feed874dcf57"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    organic_results = results["organic_results"]

    author_id = ""
    first_authors = organic_results[0]["publication_info"]["authors"]
    for author in first_authors:
        if (author["name"] == author_name):
            author_id = author["author_id"]

    # get all information on author from Author API
    params = {
        "engine" : "google_scholar_author",
        "author_id" : author_id,
        "api_key" : "c1b57a5186ae96e31b5966c89200e8fbe3491fb9854ad5089f56feed874dcf57"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    articles = results["articles"]

    print("Title,Authors,Year,Citations\n")

    total_citations = 0
    for article in articles:
        title = article["title"]
        authors = article["authors"]
        year = article["year"]
        citations = article["cited_by"]["value"]
        if (type(citations) == int):
            total_citations += citations
        else:
            citations = 0
            total_citations += citations
        
        print_string = title + ";" + authors + ";" + str(year) + ";" + str(citations)
        
        print(print_string)
    
    print("Total citations;" + str(total_citations))


    return 



