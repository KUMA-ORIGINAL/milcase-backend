from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Order(models.Model):
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Общая стоимость"
    )
    is_paid = models.BooleanField(
        default=False,
        verbose_name="Оплачен"
    )
    status = models.CharField(
        max_length=50,
        default='ожидание',
        verbose_name="Статус платежа"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name="Пользователь"
    )

    def __str__(self):
        return f"Заказ {self.id} от {self.user.email}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
