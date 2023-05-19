from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Quiz(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="название",
    )
    description = models.TextField(
        null=False,
        blank=False,
        verbose_name="описание",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "тест"
        verbose_name_plural = "тесты"


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="тест",
        related_name="questions",
    )
    text = models.TextField(
        null=False,
        blank=False,
        verbose_name="текст",
    )

    def __str__(self):
        return f"Вопрос {self.text} к тесту {self.quiz}"

    class Meta:
        verbose_name = "вопрос"
        verbose_name_plural = "вопросы"


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="вопрос",
        related_name="answers",
    )
    text = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="текст ответа",
    )
    is_correct = models.BooleanField(
        default=False,
        null=False,
        blank=True,
        verbose_name="корректно?",
    )

    def __str__(self):
        return f"Ответ на вопрос {self.question}: {self.text}"

    class Meta:
        verbose_name = "ответ на вопрос"
        verbose_name_plural = "ответы на вопросы"


class QuizResult(models.Model):
    quiz = models.ForeignKey(
        to=Quiz,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="тест",
        related_name="results",
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="пользователь",
        related_name="results",
    )
    score = models.IntegerField(verbose_name="счёт")
    total = models.IntegerField(verbose_name="итог")
    date_taken = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
        editable=False,
        verbose_name="дата прохождения",
    )

    def __str__(self):
        return f"{self.date_taken} {self.user.username} -> {self.quiz}"

    class Meta:
        verbose_name = "результат"
        verbose_name_plural = "результаты"
