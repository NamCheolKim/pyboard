from django.urls import path
from . import views

app_name = "pyboard"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("answer/create/<int:pk>/", views.answer_create, name="answer"),
    path("question/create/", views.question_create, name="question"),
    path("question/modify/<int:pk>/", views.question_modify, name="question_modify"),
    path("question/delete/<int:pk>/", views.question_delete, name="question_delete"),
    path("answer/modify/<int:pk>/", views.answer_modify, name="answer_modify"),
    path("answer/delete/<int:pk>/", views.answer_delete, name="answer_delete"),
    path(
        "comment/create/question/<int:pk>/",
        views.comment_create_question,
        name="comment_create_question",
    ),
    path(
        "comment/modify/question/<int:pk>/",
        views.comment_modify_question,
        name="comment_modify_question",
    ),
    path(
        "comment/delete/question/<int:pk>/",
        views.comment_delete_question,
        name="comment_delete_question",
    ),
    path(
        "comment/create/answer/<int:pk>/",
        views.comment_create_answer,
        name="comment_create_answer",
    ),
    path(
        "comment/modify/answer/<int:pk>/",
        views.comment_modify_answer,
        name="comment_modify_answer",
    ),
    path(
        "comment/delete/answer/<int:pk>/",
        views.comment_delete_answer,
        name="comment_delete_answer",
    ),
]