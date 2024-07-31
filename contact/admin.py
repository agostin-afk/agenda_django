from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContractAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'category', 'show'
    list_filter = 'created_date',
    ordering = ()
    search_fields = 'id', 'first_name', 'last_name',
    list_editable = 'phone', 'show'
    list_per_page = 20
    list_max_show_all = 500
    list_display_links = 'first_name',


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',
