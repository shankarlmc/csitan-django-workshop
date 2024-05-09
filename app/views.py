from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, "index.html")


def question_view(request, question_id=None):
    return render(request, "question.html")


def scoreboard_view(request):
    return render(request, "scoreboard.html")