from datetime import date

from django.db import models


class Promotion(models.Model):
    PROMO_TYPE_CHOICES = [
        ('gift', 'Подарок'),
        ('discount', 'Скидка'),
        ('cashback', 'Кэшбек'),
    ]
    name = models.CharField(max_length=255)  # Название акции
    description = models.TextField()  # Описание акции
    promo_type = models.CharField(max_length=10, choices=PROMO_TYPE_CHOICES)  # Тип акции
    start_date = models.DateField()  # Дата начала акции
    end_date = models.DateField()  # Дата окончания акции
    is_active = models.BooleanField(default=True)  # Статус активности

    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, null=True, blank=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Для скидки
    cashback_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Для кэшбека

    def is_active_for_user(self, user):
        today = date.today()
        if not self.is_active:
            return False
        if today < self.start_date or today > self.end_date:
            return False
        return True
