from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Home")


def detail(request, question_id):
    return HttpResponse(f"Estas viendo la pregunta # {question_id}")


def result(request, question_id):
    return HttpResponse(f"Estas viendo los resultados # {question_id}")



def votes(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta # {question_id}")