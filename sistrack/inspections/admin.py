from django.contrib import admin
from .models import Location, DeviceType, Device, TestInstance, Document

# Register your models here.
admin.site.register(Location)
admin.site.register(DeviceType)
#admin.site.register(Device)
#admin.site.register(TestInstance)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('location','tagnumber','description')
    list_filter = ('location','devicetype')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('doc_number','doc_name','doc_type')
    list_filter = ('doc_type',)

@admin.register(TestInstance)
class TestInstanceAdmin(admin.ModelAdmin):
    list_display = ('device','inspector','test_date', 'due_date')
    list_filter = ('inspector','result')
