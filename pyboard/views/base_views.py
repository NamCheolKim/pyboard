from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .. import models


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
