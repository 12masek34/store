from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .manager import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('Email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Category(models.Model):
    title = models.CharField('название', max_length=255)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField('название', max_length=255)
    text = models.TextField('текст')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField('автор', max_length=255, blank=True, null=True)
    image = models.ImageField('изображение', upload_to='product/%Y/%m/%d/', blank=True, null=True)
    price = models.IntegerField('цена', blank=True, null=True)
    phone = models.CharField('телефон', max_length=30)

    class Meta:
        verbose_name = 'продук'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title
