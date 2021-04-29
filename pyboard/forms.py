from django import forms
from . import models


class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = ("subject", "content")
        labels = {
            "subject": "제목",
            "content": "내용",
        }

    def save(self):
        question = super().save(commit=False)
        return question


class AnswerForm(forms.ModelForm):
    class Meta:
        model = models.Answer
        fields = ("content",)
        labels = {"content": "답변내용"}

    def save(self):
        answer = super().save(commit=False)
        return answer


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ("content",)
        labels = {"content": "댓글내용"}

    def save(self):
        comment = super().save(commit=False)
        return comment
