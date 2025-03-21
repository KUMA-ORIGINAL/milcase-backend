from django.contrib import admin

from unfold.admin import ModelAdmin as UnfoldModelAdmin, TabularInline

from ..models import Order, OrderItem


class OrderItemInline(TabularInline):
    model = OrderItem
    extra = 1
    fields = ('product', 'quantity', 'price', 'is_free')


@admin.register(Order)
class OrderAdmin(UnfoldModelAdmin):
    list_display = ['id', 'user', 'total_price', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['user__email', 'id']
    readonly_fields = ['created_at', 'updated_at']
    inlines = (OrderItemInline,)  # Добавляем вложенные элементы заказа

    fieldsets = (
        ('Основная информация', {
            'fields': ('user', 'total_price', 'discount', 'free_case_count', 'status')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Сворачиваемый блок
        }),
    )

