from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from .models import Question

def index(request):
    lates_question_list = Question.objects.all()
    return render(request, "polls/index.html", {"lates_question_list":lates_question_list})

def detail(request, question_id):
    return 

def result(request, question_id):
    return HttpResponse(f"Estas viendo los resultados # {question_id}")

def votes(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta # {question_id}")
