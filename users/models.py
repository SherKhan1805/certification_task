from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='email', unique=True)
    name = models.CharField(max_length=100, verbose_name='name')
    surname = models.CharField(max_length=100, verbose_name='surname')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email} {self.name} {self.surname}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
