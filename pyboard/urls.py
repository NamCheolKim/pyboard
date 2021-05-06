from django.urls import path
from .views import base_views, question_views, answer_views, comment_views, vote_views

app_name = "pyboard"

urlpatterns = [
    # base_views
    path("", base_views.IndexView.as_view(), name="index"),
    path("<int:pk>/", base_views.detail_view, name="detail"),
    # question_views
    path("question/create/", question_views.question_create, name="question"),
    path(
        "question/modify/<int:pk>/",
        question_views.question_modify,
        name="question_modify",
    ),
    path(
        "question/delete/<int:pk>/",
        question_views.question_delete,
        name="question_delete",
    ),
    # answer_views
    path("answer/create/<int:pk>/", answer_views.answer_create, name="answer"),
    path(
        "answer/modify/<int:pk>/",
        answer_views.answer_modify,
        name="answer_modify",
    ),
    path(
        "answer/delete/<int:pk>/",
        answer_views.answer_delete,
        name="answer_delete",
    ),
    # comment_views
    path(
        "comment/create/question/<int:pk>/",
        comment_views.comment_create_question,
        name="comment_create_question",
    ),
    path(
        "comment/modify/question/<int:pk>/",
        comment_views.comment_modify_question,
        name="comment_modify_question",
    ),
    path(
        "comment/delete/question/<int:pk>/",
        comment_views.comment_delete_question,
        name="comment_delete_question",
    ),
    path(
        "comment/create/answer/<int:pk>/",
        comment_views.comment_create_answer,
        name="comment_create_answer",
    ),
    path(
        "comment/modify/answer/<int:pk>/",
        comment_views.comment_modify_answer,
        name="comment_modify_answer",
    ),
    path(
        "comment/delete/answer/<int:pk>/",
        comment_views.comment_delete_answer,
        name="comment_delete_answer",
    ),
    # vote_views
    path(
        "vote/question/<int:pk>/",
        vote_views.vote_question,
        name="vote_question",
    ),
    path(
        "vote/answer/<int:pk>/",
        vote_views.vote_answer,
        name="vote_answer",
    ),
]
