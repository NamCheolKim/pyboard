from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .. import models
from .. import forms


@login_required(login_url="common:login")
def question_create(request):
    """PyBoard Question Create Definition"""

    if request.method == "POST":
        form = forms.QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            question.author = request.user
            question.create_date = timezone.now()
            question.save()

            return redirect(reverse("pyboard:index"))
    else:
        form = forms.QuestionForm()

    context = {"form": form}

    return render(request, "pyboard/question_form.html", context)


@login_required(login_url="common:login")
def question_modify(request, pk):
    """ PyBoard Question Modify Definition """

    question = get_object_or_404(models.Question, pk=pk)

    if request.user != question.author:
        messages.error(request, "수정권한이 없습니다.")
        return redirect(reverse("pyboard:detail", kwargs={"pk": question.pk}))

    if request.method == "POST":
        form = forms.QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save()
            question.author = request.user
            question.modify_date = timezone.now()
            question.save()
            return redirect(reverse("pyboard:detail", kwargs={"pk": question.pk}))
    else:
        form = forms.QuestionForm(instance=question)

    context = {"form": form}
    return render(request, "pyboard/question_form.html", context)


@login_required(login_url="common:login")
def question_delete(request, pk):
    """ Pyboard Question Delete Definition """

    question = get_object_or_404(models.Question, pk=pk)

    if request.user != question.author:
        messages.error(request, "삭제권한이 없습니다.")
        return redirect(reverse("pyboard:detail", kwargs={"pk": question.pk}))

    question.delete()
    return redirect(reverse("pyboard:index"))