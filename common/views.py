from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, reverse

from . import forms


def signup(request):
    """SignUp Definition"""

    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse("index"))
    else:
        form = forms.SignUpForm()
    return render(request, "common/signup.html", {"form": form})
