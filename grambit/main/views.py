from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/main.html')

def reviews(request):
    return render(request, 'main/reviews.html')

def pravila(request):
    return render(request, 'main/pravila.html')