from django.contrib import admin
from main.models import *


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
    )
    search_fields = (
        "title",
        "description",
    )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "quiz",
    )
    list_filter = ("quiz__title",)
    search_fields = (
        "text",
        "quiz__title",
        "quiz__description",
    )


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "is_correct",
        "question",
    )
    list_filter = (
        "is_correct",
        "question__quiz__title",
    )


@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = (
        "date_taken",
        "user",
        "quiz",
        "score",
        "total",
    )
    list_filter = (
        "date_taken",
        "user",
        "quiz__title",
    )
