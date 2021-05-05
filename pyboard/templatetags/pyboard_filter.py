import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# 페이지를 넘겨도 게시물 번호가 1로 시작하지 않고 다음 번호로 표출
@register.filter
def sub(total, previous):
    return total - previous


# 마크다운
@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))
