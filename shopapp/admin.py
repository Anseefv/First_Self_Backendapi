from django.contrib import admin
from django.contrib.auth.hashers import make_password
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ['username', 'email', 'role']

    fields = ['username', 'email', 'password', 'phone', 'age', 'place', 'role']

    def save_model(self, request, obj, form, change):

        if not change:
            obj.password = make_password(obj.password)

        super().save_model(request, obj, form, change)