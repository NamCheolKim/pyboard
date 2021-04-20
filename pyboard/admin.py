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
