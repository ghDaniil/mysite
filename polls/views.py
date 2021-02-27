from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<p>alive</p>")
def meme(request):
    return HttpResponse('<img src="https://w7.pngwing.com/pngs/892/977/png-transparent-bicycle-wheels-cycling-minibike-motorcycle-gears-bicycle-motorcycle-transport.png">')
# Create your views here.
