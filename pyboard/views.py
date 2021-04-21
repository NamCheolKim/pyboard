from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from . import models
from django.utils import timezone


class IndexView(ListView):
    """PyBoard List Definition"""

    def get_queryset(self):
        return models.Question.objects.order_by("-create_date")


class DetailView(DetailView):
    """PyBoard Detail Definition"""

    model = models.Question


def answer_create(request, pk):
    """PyBoard Answer Definition"""

    question = get_object_or_404(models.Question, pk=pk)
    answer = models.Answer(
        question=question,
        content=request.POST.get("content"),
        create_date=timezone.now(),
    )
    answer.save()

    return redirect(reverse("pyboard:detail", kwargs={"pk": question.pk}))
