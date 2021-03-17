from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# admin 패널에서 user에 대해 표현할 것을 나타냄(아래 annotation)
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """
    fieldsets = UserAdmin.fieldsets + (
        (
            "CustomField",
            {
                "fields": ("avatar", "gender", "bio", "birthdate", "language", "currency", "superhost")
            }
        ),
    )
