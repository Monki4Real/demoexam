from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils import timezone


ROLE = (
    ('Админ', 'Админ'),
    ('Пользователь', 'Пользователь'),
)

STATUS = (
    ('Новое','Новое'),
    ('Принято','Принято'),
    ('Отклонено','Отклонено'),
)

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True, blank=False, null=False, verbose_name='Логин')
    fullname = models.CharField(max_length=255, blank=False, null=False, verbose_name='ФИО')
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False, verbose_name='Почта') 
    phone_number = models.CharField("Телефон",max_length=30,null=False,blank=False,validators=[RegexValidator(regex=r"\+7\(\d\d\d\)-\d\d\d-\d\d-\d\d",message="Введите телефон в формате +7(XXX)-XXX-XX-XX",code="invalid_phone_number",),],)
    password = models.CharField(max_length=255, blank=False, verbose_name='Пароль')
    role = models.CharField(choices=ROLE, verbose_name='Роль', default='Пользователь', max_length=255)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.fullname
    

# models.py

from django.db import models

class Statement(models.Model):
    title = models.CharField(max_length=15, blank=False, null=False, verbose_name='Номер машины')
    body = models.CharField(max_length=15, blank=False, null=False, verbose_name='Описание нарушения')
    status = models.CharField(choices=STATUS, default='Новое', max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(verbose_name='Дата и время', help_text='Выберите дату и время в диапазоне 8:00 - 21:00', null=False, blank=False, default=timezone.now())


    ordering = ['created_at']

    def __str__(self):
        return self.title
