from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<p>alive</p>")

# Create your views here.
