from django.shortcuts import render, redirect
from .models import Question
# Create your views here.


def get_next_question_id(questions, played_questions):
    remaining_questions = []
    
    played_questions = [tuple(res) for res in played_questions]    
    played_questions_ids = [question for question, _ in played_questions]
        
    remaining_questions = [question_id for question_id in questions if question_id not in played_questions_ids]
        
    if remaining_questions:
        return str(remaining_questions[0])
        
    return '0'


def home_view(request):
    """Renders index.html with user info"""
    session_user_info = request.session.get("player_name", None)
    questions = Question.objects.all()
    
    question_ids = [str(question.id) for question in questions]
    request.session["question_ids"] = question_ids
    request.session["played_questions"] = []
        
    if request.method == "POST":
        user_name = request.POST["name"]
        request.session["player_name"] = user_name
        
        next_question_id = get_next_question_id(
            request.session["question_ids"],
            request.session["played_questions"]
        )
        return redirect("question", question_id=next_question_id)

    context = {
        "player_name":session_user_info
    }
    return render(request, "index.html", context)


def question_view(request, question_id=None):
    if question_id == '0':
        return redirect("scoreboard")
    
    question = Question.objects.get(id=question_id)
    played_questions = request.session.get("played_questions", [])
    
    if request.method == "POST":
        answer_id = request.POST["answer"]
        played_questions.append((str(question_id), str(answer_id)))
        request.session["played_questions"] = played_questions
        
        # redirect to next question_id
        next_question_id = get_next_question_id(
            request.session["question_ids"],
            request.session["played_questions"]
        )
        return redirect("question", question_id=next_question_id)
    
    context = {
        "question": question,
        "total_no_of_questions":len(request.session.get("question_ids", [])),
        "played_questions": len(request.session["played_questions"]) +1
    }
    return render(request, "question.html", context)


def scoreboard_view(request):
    """View scoreboard"""
    played_questions = request.session["played_questions"]
    question_ids = request.session["question_ids"]
    correct_answer = 0
    
    played_questions = [tuple(res) for res in played_questions]    
    
    for question, answer in played_questions:
        ques = Question.objects.get(id=question)
        if str(ques.answer.id) == answer:
            correct_answer += 1
            
    context = {
        "correct_answer": correct_answer,
        "total_questions": len(question_ids)
    }
    
    return render(request, "scoreboard.html", context)


def reset_game(request):
    del request.session["question_ids"]
    del request.session["played_questions"]
    del request.session["player_name"]
    return redirect("home")