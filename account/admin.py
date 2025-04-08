from django.contrib import admin
from .models import UserToken

class UserTokenAdmin(admin.ModelAdmin):
    list_display = ('user','token','expiration_date', 'used', 'expired')
    list_filter = ("used", "expired", "expiration_date")
    search_fields = ['user']
    
admin.site.register(UserToken, UserTokenAdmin)