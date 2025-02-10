from django.contrib import admin

from unfold.admin import ModelAdmin as UnfoldModelAdmin

from promotions.models import Promotion


@admin.register(Promotion)
class PromotionAdmin(UnfoldModelAdmin):
    list_display = ('name', 'promo_type', 'start_date', 'end_date', 'is_active')
    search_fields = ('name', 'promo_type')
    list_filter = ('promo_type', 'is_active')
