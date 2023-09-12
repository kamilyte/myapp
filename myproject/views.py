from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name' : 'Kamile',
        'age' : 20,
        'nationality' : 'Lit'
    }

    return render(request, 'index.html', context)

def printCSV(request):
    
    print("Title,Authors,Year,Citations\n")
    