from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
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

def vote(request, q_id):
    choices=request.POST.getlist('choice')
    question = Question.objects.get(pk=q_id)
    for c_pk in choices:
        choice = question.choice_set.get(pk=c_pk)
        choice.votes +=1
        choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(q_id,) ) )


def results(request, q_id):
    questions = Question.objects.get(pk=q_id)
    context ={
        "questions":questions
    }
    return render(request,"polls/results.html",context)