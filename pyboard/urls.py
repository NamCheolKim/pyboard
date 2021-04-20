from django.urls import path
from . import views

app_name = "pyboard"
urlpatterns = [
    path("", views.index, name="index"),
]