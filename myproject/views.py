from django.shortcuts import render
from serpapi import GoogleSearch


def googleSearch(request):

    # check request method
    if request.method =="POST":
        print(request.POST.get('name'))
        name = request.POST.get('name')
    else:
        print("GET")
        name = ""

    myHTML = "" # empty html script

    if (request.POST.get('name') != ""):

        # get author ID from Google Scholar API
        split_name = name.split()
        first_letter = split_name[0][0]
        surname = split_name[1]
        author_name = first_letter + " " + surname
        print(author_name)
        params = {
            "engine" : "google_scholar",
            "q" : "author: " + name,
            "api_key" : "c1b57a5186ae96e31b5966c89200e8fbe3491fb9854ad5089f56feed874dcf57"
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        organic_results = results["organic_results"]
        author_id = ""
        idx = 0
        flag = False
        while (flag == False):
            test_authors = organic_results[idx]["publication_info"]["authors"]

            for author in test_authors:
                if (author["name"] == author_name):
                    author_id = author["author_id"]
                    flag = True 
            idx += 1

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
            myHTML += "<tr><td> " + name + " </td><td>" + authors + "</td><td>" + str(year) + "</td><td>" + str(citations) + "</td></tr>"
    
        print("Total citations;" + str(total_citations))

    return render(request, 'index.html', {"myHTML" : myHTML})


