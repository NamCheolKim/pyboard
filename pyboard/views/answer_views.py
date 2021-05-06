from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse, resolve_url
from django.utils import timezone
from .. import models
from .. import forms


@login_required(login_url="common:login")
def answer_create(request, pk):
    """PyBoard Answer Create Definition"""

    question = get_object_or_404(models.Question, pk=pk)

    if request.method == "POST":
        form = forms.AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()

            return redirect(
                "{}#answer_{}".format(
                    resolve_url("pyboard:detail", pk=question.pk), answer.pk
                )
            )
    else:
        form = forms.AnswerForm()

    context = {"question": question, "form": form}

    return render(request, "pyboard/question_detail.html", context)


@login_required(login_url="common:login")
def answer_modify(request, pk):
    """ Pyboard Answer Modify Definition """

    answer = get_object_or_404(models.Answer, pk=pk)

    if request.user != answer.author:
        messages.error(request, "수정권한이 없습니다.")
        return redirect(reverse("pyboard:detail", kwargs={"pk": answer.question.pk}))

    if request.method == "POST":
        form = forms.AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save()
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()

            return redirect(
                "{}#answer_{}".format(
                    resolve_url("pyboard:detail", pk=answer.question.pk), answer.pk
                )
            )
    else:
        form = forms.AnswerForm(instance=answer)

    context = {"answer": answer, "form": form}

    return render(request, "pyboard/answer_form.html", context)


@login_required(login_url="common:login")
def answer_delete(request, pk):
    """ Pyboard Answer Delete Definition """

    answer = get_object_or_404(models.Answer, pk=pk)

    if request.user != answer.author:
        messages.error(request, "삭제권한이 없습니다.")
    else:
        answer.delete()
    return redirect(reverse("pyboard:detail", kwargs={"pk": answer.question.pk}))
