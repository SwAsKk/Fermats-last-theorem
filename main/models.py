from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)