from django.contrib import admin

from unfold.admin import ModelAdmin as UnfoldModelAdmin, TabularInline

from ..models import Order, OrderItem


class OrderItemInline(TabularInline):
    model = OrderItem
    extra = 1
    fields = ('product', 'quantity', 'price')


@admin.register(Order)
class OrderAdmin(UnfoldModelAdmin):
    list_display = ['id', 'user', 'total_price', 'status', 'created_at', 'is_paid']
    list_filter = ['is_paid', 'status', 'created_at']
    search_fields = ['user__email', 'id']
    readonly_fields = ['created_at', 'updated_at']
    inlines = (OrderItemInline,)  # Добавляем вложенные элементы заказа

    fieldsets = (
        ('Основная информация', {
            'fields': ('user', 'total_price', 'status', 'is_paid')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Сворачиваемый блок
        }),
    )

