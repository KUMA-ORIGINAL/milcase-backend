from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = 'ожидание', 'Ожидает'
        PAID = 'оплачен', 'Оплачен'
        CANCELLED = 'отменен', 'Отменен'

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Общая стоимость"
    )
    status = models.CharField(
        max_length=50,
        choices=Status,
        default=Status.PENDING,
        verbose_name="Статус платежа",
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name="Пользователь"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )

    def __str__(self):
        return f"Заказ {self.id} от {self.user.email}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
