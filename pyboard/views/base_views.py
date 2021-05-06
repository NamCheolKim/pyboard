from django.core.paginator import Paginator
from django.views.generic import ListView
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404
from .. import models


class IndexView(ListView):
    """PyBoard IndexView Definition"""

    def get(self, request):

        # 페이지
        page = request.GET.get("page", 1)

        # 검색어
        kw = request.GET.get("kw", "")

        # 정렬 기준
        so = request.GET.get("so", "recent")

        # 정렬
        if so == "recommend":
            question_list = models.Question.objects.annotate(
                num_voter=Count("voter")
            ).order_by("-num_voter", "-create_date")
        elif so == "popular":
            question_list = models.Question.objects.annotate(
                num_answer=Count("answer")
            ).order_by("-num_answer", "-create_date")
        else:
            question_list = models.Question.objects.order_by("-create_date")

        # 조회
        if kw:
            question_list = question_list.filter(
                Q(subject__icontains=kw)
                | Q(content__icontains=kw)
                | Q(author__username__icontains=kw)
                | Q(author__username__icontains=kw)
                | Q(answer__author__username__icontains=kw)
            ).distinct()

        # 페이징
        paginator = Paginator(question_list, 10)  # 1페이지당 10건의 게시물 표출
        page_obj = paginator.get_page(page)

        context = {"question_list": page_obj, "page": page, "kw": kw, "so": so}

        return render(request, "pyboard/question_list.html", context)


def detail_view(request, pk):

    """PyBoard DetailView Definition"""

    page = request.GET.get("page", "1")  # 페이지
    so = request.GET.get("so", "recommend")
    question = get_object_or_404(models.Question, pk=pk)

    # 답변 정렬
    answer_list = models.Answer.objects.filter(question=question).annotate(
        num_voter=Count("voter")
    )
    if so == "recommend":
        answer_list = answer_list.order_by("-num_voter", "-create_date")
    else:  # 시간순으로 정렬
        answer_list = answer_list.order_by("-create_date", "-num_voter")

    # 답변 페이징
    paginator = Paginator(answer_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {
        "question": question,
        "answer_list": page_obj,
        "page": page,
        "so": so,
    }
    return render(request, "pyboard/question_detail.html", context)
