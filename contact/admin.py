from django.contrib import admin
from .models import Contact, CommunicationLog

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    list_filter = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')

class CommunicationLogAdmin(admin.ModelAdmin):
    list_display = ('contact', 'type', 'date')
    list_filter = ('contact', 'type', 'date')
    search_fields = ('contact', 'type', 'date')

admin.site.register(Contact, ContactAdmin)
admin.site.register(CommunicationLog, CommunicationLogAdmin)