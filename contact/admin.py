from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContractAdmin(admin.ModelAdmin):
    ...
