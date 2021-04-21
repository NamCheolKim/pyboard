from django.urls import path
from . import views

app_name = "pyboard"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("answer/create/<int:pk>/", views.answer_create, name="answer"),
]