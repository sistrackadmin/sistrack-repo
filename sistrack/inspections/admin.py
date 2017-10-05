from django.contrib import admin
from .models import Location, DeviceType, Device, TestInstance, Document, Interlock, Ipl

# Register your models here.
#admin.site.register(Location)
admin.site.register(DeviceType)
#admin.site.register(Device)
#admin.site.register(TestInstance)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('unit','description', 'area', 'plant')
    list_filter = ('area','plant')

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('location','tagnumber','description')
    list_filter = ('location','devicetype')
    search_fields = ['tagnumber', 'description']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('doc_number','doc_name','doc_type')
    list_filter = ('doc_type',)

@admin.register(TestInstance)
class TestInstanceAdmin(admin.ModelAdmin):
    list_display = ('device','inspector','test_date', 'due_date')
    list_filter = ('inspector','result')

@admin.register(Interlock)
class InterlockAdmin(admin.ModelAdmin):
    list_display = ('interlock_unit','interlock_number','interlock_description')
    list_filter = ('interlock_unit',)

@admin.register(Ipl)
class IplAdmin(admin.ModelAdmin):
    list_display = ('ipl_unit','initiator', 'ipl_description')
    list_filter = ('ipl_unit',)
