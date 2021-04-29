from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
from . import models
from django.utils import timezone
from . import forms


class IndexView(ListView):
    """PyBoard IndexView Definition"""

    def get(self, request):
        # 조회
        question_list = models.Question.objects.order_by("-create_date")

        # 페이지
        page = request.GET.get("page", 1)

        # 페이징
        paginator = Paginator(question_list, 10)  # 1페이지당 10건의 게시물 표출
        page_obj = paginator.get_page(page)

        context = {"question_list": page_obj}

        return render(request, "pyboard/question_list.html", context)


class DetailView(DetailView):
    """PyBoard DetailView Definition"""

    model = models.Question


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

            return redirect(reverse("pyboard:detail", kwargs={"pk": question.pk}))
    else:
        form = forms.AnswerForm()

    context = {"question": question, "form": form}

    return render(request, "pyboard/question_detail.html", context)


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
                reverse("pyboard:detail", kwargs={"pk": answer.question.pk})
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

            return redirect(reverse("pyboard:detail", kwargs={"pk": question.pk}))
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
                reverse("pyboard:detail", kwargs={"pk": comment.question.pk})
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

            return redirect(reverse("pyboard:detail", kwargs={"pk": comment.answer.question.pk}))
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
        return redirect(reverse("pyboard:detail", kwargs={"pk": comment.answer.question.pk}))

    if request.method == "POST":
        form = forms.CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect(
                reverse("pyboard:detail", kwargs={"pk": comment.answer.question.pk})
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
        return redirect(reverse("pyboard:detail", kwargs={"pk": comment.answer.question.pk}))
    else:
        comment.delete()

    return redirect(reverse("pyboard:detail", kwargs={"pk": comment.answer.question.pk}))
