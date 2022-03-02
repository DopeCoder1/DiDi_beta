from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    author = models.ForeignKey("Author", on_delete=models.CASCADE, verbose_name="Автор")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name="Категория")
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(max_length=100, db_index=True)
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Последний изм.")
    rating = models.IntegerField(default=5,verbose_name="rating")
    published_status = models.IntegerField(default=0, verbose_name="Публиковать?")
    desc = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

class MainCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(max_length=150, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Главное Категория"
        verbose_name_plural = "Главные Категории"

class Category(models.Model):
    maincategory = models.ForeignKey(MainCategory, on_delete=models.CASCADE, verbose_name="Главное Категория")
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(max_length=150, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    desc = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to="author_photos/%Y/%m/%d/", verbose_name="Фото")

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"