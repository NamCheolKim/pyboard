from django import template

register = template.Library()

# 페이지를 넘겨도 게시물 번호가 1로 시작하지 않고 다음 번호로 표출
@register.filter
def sub(total, previous):
    return total - previous