from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Contact
from import_export.admin import ImportExportModelAdmin


# class ContactAdmin(admin.ModelAdmin):
class ContactAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'gender', 'info', 'date_added', 'image')
    list_display_links = ('id', 'name')
    list_editable = ('info',)
    list_per_page = 8
    search_fields = ('name', 'email', 'phone', 'info')
    list_filter = ('gender', 'date_added')


admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)
