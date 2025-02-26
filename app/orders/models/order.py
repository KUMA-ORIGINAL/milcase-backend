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
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, verbose_name='Скидка')
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

    def apply_birthday_discount(self):
        user_profile = self.user.profile  # Профиль пользователя
        birthday_discount = user_profile.get_birthday_discount()

        if birthday_discount:
            discount_amount = (self.total_price * birthday_discount) / 100
            self.discount = round(discount_amount)  # Округляем скидку до целого числа

            self.total_price -= self.discount  # Применяем скидку к общей стоимости

            self.total_price = round(self.total_price)

        self.save()