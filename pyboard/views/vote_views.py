from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, reverse
from .. import models


@login_required(login_url="common:login")
def vote_question(request, pk):
    """ PyBoard Vote Question Definition """

    question = get_object_or_404(models.Question, pk=pk)
    if request.user == question.author:
        messages.info(request, "본인이 작성한 게시물은 추천할 수 없습니다.")
    else:
        question.voter.add(request.user)

    return redirect(reverse("pyboard:detail", kwargs={"pk": question.pk}))


@login_required(login_url="common:login")
def vote_answer(request, pk):
    """ PyBoard Vote Answer Definition """

    answer = get_object_or_404(models.Answer, pk=pk)
    if request.user == answer.author:
        messages.info(request, "본인이 작성한 게시물은 추천할 수 없습니다.")
    else:
        answer.voter.add(request.user)

    return redirect(reverse("pyboard:detail", kwargs={"pk": answer.question.pk}))
