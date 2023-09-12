from django.shortcuts import render
from django.http import HttpResponse

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

