from django.contrib import admin
from django.shortcuts import redirect
from django.urls import reverse

from unfold.admin import ModelAdmin as UnfoldModelAdmin

from promotions.models import BirthdayDiscountSettings


@admin.register(BirthdayDiscountSettings)
class BirthdayDiscountSettingsAdmin(UnfoldModelAdmin):
    list_display = ('discount_percentage',)

    def has_add_permission(self, request):
        if BirthdayDiscountSettings.objects.exists():
            return False
        return super().has_add_permission(request)
