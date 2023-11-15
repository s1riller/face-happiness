# abstract_user/users/models.py
import requests
from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(
        'Аватар',
        upload_to='avatars/',
        default='avatars/awesomeAvatar.png',  # Путь к изображению по умолчанию
        blank=True,
    )

    processed_photo = models.BooleanField(verbose_name='Обработанное фото',
                                          default=False)


class Imperfection(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class SkinType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class CategoryProduct(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='')

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    treats = models.ForeignKey(Answer, on_delete=models.CASCADE, default=None, null=True)
    img = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, default=1)

def __str__(self):
        return self.name


class UserTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answers = models.JSONField()
    time = models.TimeField()
    medicine = models.TextField(default='')



