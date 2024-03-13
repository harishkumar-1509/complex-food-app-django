from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin 
# Register your models here.

class CustomUserAdmin(UserAdmin):
    # Below are implementations to make the password field non-editable in django admin panel.
    list_display = ('email','first_name','last_name','username','role','is_active',)
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User)
admin.site.register(UserProfile)