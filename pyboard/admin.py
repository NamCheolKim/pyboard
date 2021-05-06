from django.contrib import admin
from . import models


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):

    """ Question Admin Definition """

    list_display = (
        "subject",
        "create_date",
    )
    search_fields = ["subject"]


# @admin.register(models.Category)
# class CategoryAdmin(admin.ModelAdmin):

#     """ Category Admin Definition """

#     list_display = (
#         "name",
#         "description",
#         "has_answer",
#     )
