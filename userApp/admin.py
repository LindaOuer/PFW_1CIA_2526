from django.contrib import admin

from userApp.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'first_name', 'last_name', 'affiliation', 'nationality', 'role')

admin.site.register(User, UserAdmin)
