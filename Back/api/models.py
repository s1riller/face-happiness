# abstract_user/users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    birth_date = models.DateField(null=True, blank=True)
    REQUIRED_FIELDS = ['birth_date']


class Imperfection(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class SkinType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.CharField(max_length=200)  # The text of the question

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Relationship with Question
    text = models.CharField(max_length=200)  # The text of the answer

    def __str__(self):
        return self.text


class Medicine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    treats = models.ForeignKey(Imperfection, on_delete=models.CASCADE)
    img = models.TextField(default='')

    def __str__(self):
        return self.name


class UserTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Предположим, что у вас есть модель User
    answers = models.JSONField()  # Используем JSONField для хранения ответов
    time = models.TimeField(auto_now=True)
    medicine = models.TextField(default='')

    # Дополнительные поля, если необходимо
