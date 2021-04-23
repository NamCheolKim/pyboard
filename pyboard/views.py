from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
from . import models
from django.utils import timezone
from . import forms


class IndexView(ListView):
    """PyBoard List Definition"""

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
    """PyBoard Detail Definition"""

    model = models.Question


def answer_create(request, pk):
    """PyBoard Answer Definition"""

    question = get_object_or_404(models.Question, pk=pk)

    if request.method == "POST":
        form = forms.AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()

            return redirect(reverse("pyboard:detail", kwargs={"pk": question.pk}))
    else:
        form = forms.AnswerForm()

    context = {"question": question, "form": form}

    return render(request, "pyboard/question_detail.html", context)


def question_create(request):
    """PyBoard Question Definition"""

    if request.method == "POST":
        form = forms.QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            question.create_date = timezone.now()
            question.save()

            return redirect(reverse("pyboard:index"))
    else:
        form = forms.QuestionForm()

    context = {"form": form}

    return render(request, "pyboard/question_form.html", context)
