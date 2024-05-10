from django.shortcuts import render, redirect
from .models import Question
# Create your views here.


def home_view(request):
    """Renders index.html with user info"""
    session_user_info = request.session.get("player_name", None)
    if request.method == "POST":
        user_name = request.POST["name"]
        request.session["player_name"] = user_name
        return redirect("question", question_id=1)
        
    context = {
        "player_name":session_user_info
    }
    return render(request, "index.html", context)


def question_view(request, question_id=None):
    question = Question.objects.get(id=question_id)
    context = {
        "question": question
    }
    return render(request, "question.html", context)


def scoreboard_view(request):
    return render(request, "scoreboard.html")