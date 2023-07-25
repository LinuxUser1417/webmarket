from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator



User = get_user_model()


class Category(models.Model):
    name = models.CharField(verbose_name="Название категории", max_length=100)
    description = models.TextField(verbose_name="Описание категории")


class Product(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID товара", unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products",verbose_name="Владелец товара")
    title = models.CharField(verbose_name="Заголовок товара", max_length=255)
    name = models.CharField(verbose_name="Название товара", max_length=255)
    description = models.TextField(verbose_name="Описание товара")
    price = models.FloatField(verbose_name="Цена товара")
    stock = models.PositiveSmallIntegerField(verbose_name="Количество Товара")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")
    categories = models.ManyToManyField(Category, verbose_name="Категории товара")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение товара")

    def __str__(self):
        return self.title


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews"  ,verbose_name="Товар")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    content = models.TextField(verbose_name="Содержание отзыва")
    rating = models.PositiveSmallIntegerField( validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="Рейтинг")

    def __str__(self):
        return self.content

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites"  ,verbose_name="Пользователь")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="favorites"  ,verbose_name="Товар")
    favorite = models.BooleanField(default=False, verbose_name="Избранное")

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"
    
