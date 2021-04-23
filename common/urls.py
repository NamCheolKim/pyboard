from django.urls import path
from django.contrib.auth import views

app_name = "common"

urlpatterns = [
    path(
        "login/",
        views.LoginView.as_view(template_name="common/login.html"),
        name="login",
    ),
]
