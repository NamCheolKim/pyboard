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
]