from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views import generic


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name="questions"
    
    
    def get_queryset(self):
        return Question.objects.all()

class DetailView(generic.DetailView):
    model= Question
    template_name = "polls/detail.html"
    

class ResultsView(generic.DetailView):
    template_name = "polls/results.html"
    model= Question

def vote(request, q_id):
    choices=request.POST.getlist('choice')
    question = Question.objects.get(pk=q_id)
    for c_pk in choices:
        choice = question.choice_set.get(pk=c_pk)
        choice.votes +=1
        choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(q_id,) ) )



