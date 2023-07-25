from django.contrib import admin
from .models import Category, Product, Review, Favorite

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Favorite)
