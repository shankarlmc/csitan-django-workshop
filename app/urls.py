from django.urls import path
from . import views

urlpatterns = [
    path("",views.home_view, name="home"),
    
    path("question/<str:question_id>/",views.question_view, name="question"),
    
    path("scoreboard/",views.scoreboard_view, name="scoreboard"),
    path("reset-game/",views.reset_game, name="reset_game"),
]