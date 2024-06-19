from django.contrib import admin

from . import models


@admin.register(models.DeliveryPoint)
class DeliveryPointAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'phones', 'type', 'owner_code', 'created', 'updated']
    search_fields = ['uuid', 'code', 'city__id', 'city__name']
    # list_filter = ('city__id',)
    raw_id_fields = ['city']
    list_select_related = ['city']
