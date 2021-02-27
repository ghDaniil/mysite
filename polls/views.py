from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice


def index(request):
    q_all = Question.objects.all()
    res = "<ol>"
    for q in q_all:
        res += "<li>%s</li>"% q.text
    res += "</ol>"

    return HttpResponse(res)
def meme(request):
    return HttpResponse('<img src="https://w7.pngwing.com/pngs/892/977/png-transparent-bicycle-wheels-cycling-minibike-motorcycle-gears-bicycle-motorcycle-transport.png">')
# Create your views here.

def detail(request, q_id):
    res = "Question number %s." %q_id
    return HttpResponse(res)

def results(request, q_id):
    res = "Result for question number %s." %q_id
    return HttpResponse(res)

def vote(request, q_id):
    res = "Vote for question number %s." %q_id
    return HttpResponse(res)
