from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User)

# or
# @admin.register(User)
# class UserAdmin(UserAdmin):
  
#   fieldsets = UserAdmin.fieldsets
