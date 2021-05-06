from django.contrib.auth.models import User
from django.db import models


# class Category(models.Model):
#     name = models.CharField(max_length=20, unique=True)
#     description = models.CharField(max_length=200, null=True, blank=True)
#     has_answer = models.BooleanField(default=True)  # 답변가능 여부

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name_plural = "Categories"


class Question(models.Model):
    class Meta:
        ordering = ["id"]

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_question"
    )
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name="voter_question")
    # category = models.ForeignKey(
    #     Category, on_delete=models.CASCADE, related_name="category_question"
    # )
    view_count = models.IntegerField(null=True, blank=True, default=0)
    notice = models.BooleanField(default=False)  # 공지사항 여부

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_answer"
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name="voter_answer")


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(
        Question, null=True, blank=True, on_delete=models.CASCADE
    )
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
