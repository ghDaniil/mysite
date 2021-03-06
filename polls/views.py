from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice


def index(request):
    questions =Question.objects.all()
    context = {
        "adminName":"danil",
        "questions": questions
    }

    return render(request,"polls/index.html",context)

def meme(request):
    return HttpResponse('<img src="https://w7.pngwing.com/pngs/892/977/png-transparent-bicycle-wheels-cycling-minibike-motorcycle-gears-bicycle-motorcycle-transport.png">')
# Create your views here.

def detail(request, q_id):
    questions = Question.objects.get(pk=q_id)
    context ={
        "questions":questions
    }
    return render(request,"polls/detail.html",context)
def results(request, q_id):
    res = "Result for question number %s." %q_id
    return HttpResponse(res)

def vote(request, q_id):
    res = "Vote for question number %s." %q_id
    return HttpResponse(res)
