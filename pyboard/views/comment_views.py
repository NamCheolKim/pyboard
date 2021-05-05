from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse, resolve_url
from django.utils import timezone
from .. import models
from .. import forms


@login_required(login_url="common:login")
def comment_create_question(request, pk):
    """ Pyboard Comment Create Definition """

    question = get_object_or_404(models.Question, pk=pk)
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.question = question
            comment.save()

            return redirect(
                "{}#comment_{}".format(
                    resolve_url("pyboard:detail", pk=comment.question.pk), comment.pk
                )
            )
    else:
        form = forms.CommentForm()
    context = {"form": form}
    return render(request, "pyboard/comment_form.html", context)


@login_required(login_url="common:login")
def comment_modify_question(request, pk):
    """ Pyboard Comment Modify Definition """
    comment = get_object_or_404(models.Comment, pk=pk)

    if request.user != comment.author:
        messages.error(request, "댓글 수정 권한이 없습니다.")
        return redirect(reverse("pyboard:detail", kwargs={"pk": comment.question.pk}))

    if request.method == "POST":
        form = forms.CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()

            return redirect(
                "{}#comment_{}".format(
                    resolve_url("pyboard:detail", pk=comment.question.pk), comment.pk
                )
            )
    else:
        form = forms.CommentForm(instance=comment)
    context = {"form": form}
    return render(request, "pyboard/comment_form.html", context)


@login_required(login_url="common:login")
def comment_delete_question(request, pk):
    """ Pyboard Comment Delete Definition """

    comment = get_object_or_404(models.Comment, pk=pk)

    if request.user != comment.author:
        messages.error(request, "댓글 삭제 권한이 없습니다.")
        return redirect(reverse("pyboard:detail", kwargs={"pk": comment.question.pk}))
    else:
        comment.delete()

    return redirect(reverse("pyboard:detail", kwargs={"pk": comment.question.pk}))


@login_required(login_url="common:login")
def comment_create_answer(request, pk):
    """ Pyboard Comment Create Definition """

    answer = get_object_or_404(models.Answer, pk=pk)
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()

            return redirect(
                "{}#comment_{}".format(
                    resolve_url("pyboard:detail", pk=comment.answer.question.pk), comment.pk
                )
            )
    else:
        form = forms.CommentForm()
    context = {"form": form}
    return render(request, "pyboard/comment_form.html", context)


@login_required(login_url="common:login")
def comment_modify_answer(request, pk):
    """ Pyboard Comment Modify Definition """
    comment = get_object_or_404(models.Comment, pk=pk)

    if request.user != comment.author:
        messages.error(request, "댓글 수정 권한이 없습니다.")
        return redirect(
            reverse("pyboard:detail", kwargs={"pk": comment.answer.question.pk})
        )

    if request.method == "POST":
        form = forms.CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            
            return redirect(
                "{}#comment_{}".format(
                    resolve_url("pyboard:detail", pk=comment.answer.question.pk), comment.pk
                )
            )
    else:
        form = forms.CommentForm(instance=comment)
    context = {"form": form}
    return render(request, "pyboard/comment_form.html", context)


@login_required(login_url="common:login")
def comment_delete_answer(request, pk):
    """ Pyboard Comment Delete Definition """

    comment = get_object_or_404(models.Comment, pk=pk)

    if request.user != comment.author:
        messages.error(request, "댓글 삭제 권한이 없습니다.")
        return redirect(
            reverse("pyboard:detail", kwargs={"pk": comment.answer.question.pk})
        )
    else:
        comment.delete()

    return redirect(
        reverse("pyboard:detail", kwargs={"pk": comment.answer.question.pk})
    )
