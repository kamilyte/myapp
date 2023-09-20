from django.shortcuts import render
from serpapi import GoogleSearch

def googleSearch(request):

    total_citations = 0  # Initialize the total_citations variable
    myHTML = ""  # Empty HTML script

    if request.method == "POST":
        name = request.POST.get('name')
    else:
        print("GET")
        name = ""

    if name.strip():
        split_name = name.split()

        if len(split_name) >= 2:
            first_letter = split_name[0][0]
            surname = split_name[1]
            author_name = first_letter + " " + surname

            params = {
                "engine": "google_scholar",
                "q": "author:" + name,
                "api_key": "c1b57a5186ae96e31b5966c89200e8fbe3491fb9854ad5089f56feed874dcf57",
            }

            search = GoogleSearch(params)
            results = search.get_dict()
            organic_results = results["organic_results"]
            author_id = ""
            idx = 0
            flag = False

            while flag == False:
                test_authors = organic_results[idx]["publication_info"]["authors"]

                for author in test_authors:
                    if author["name"] == author_name:
                        author_id = author["author_id"]
                        flag = True
                idx += 1

            start = 0  # Initialize start parameter for pagination
            num = 20   # Number of results per page (API limit)

            while True:
                params = {
                    "engine": "google_scholar_author",
                    "author_id": author_id,
                    "start": start,  # Update start parameter
                    "num": num,      # Number of results per page
                    "api_key": "c1b57a5186ae96e31b5966c89200e8fbe3491fb9854ad5089f56feed874dcf57",
                }

                search = GoogleSearch(params)
                results = search.get_dict()
                articles = results.get("articles", [])

                if not articles:  # Break the loop if no more articles are returned
                    break

                for article in articles:
                    title = article["title"]
                    authors = article["authors"]
                    year = article["year"]
                    citations = article["cited_by"]["value"]

                    if type(citations) == int:
                        total_citations += citations

                    myHTML += f"<tr><td>{title}</td><td>{name}</td><td>{authors}</td><td>{year}</td><td>{citations}</td></tr>"

                start += num  # Update the start parameter for the next page

            return render(request, 'index.html', {"myHTML": myHTML, "total_citations": total_citations})

        else:
            print("Name should have a first name and a surname.")
            return render(request, 'index.html', {"myHTML": "", "total_citations": 0})

    else:
        print("Name is empty or not valid.")
        return render(request, 'index.html', {"myHTML": "", "total_citations": 0})

    return render(request, 'index.html', {"myHTML": myHTML, "total_citations": total_citations})
