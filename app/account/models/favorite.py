from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product  # Импортируй модель продукта, если она есть

User = get_user_model()

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorited_by')

    class Meta:
        unique_together = ('user', 'product')  # Чтобы продукт мог быть в избранном только у одного пользователя

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
