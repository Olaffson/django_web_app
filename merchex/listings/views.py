from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Band, Listings


def hello(request):
    bands = Band.objects.all()
    return render(request, 
                  'listings/hello.html', 
                  context={'bands': bands})


def listings(request):
    listings = Listings.objects.all()
    return render(request, 
                  'listings/listings.html', 
                  context={'listings': listings})


def about(request):
    return render(request, 
                  'listings/about.html')
    # return HttpResponse('<h1>A propos</h1> <p>Je suis un grand fan de django, hahaha ...</p>')
