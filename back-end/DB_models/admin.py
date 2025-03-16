from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Talent_dsc, Talent, Project, Contract

# Реєструємо модель користувача з кастомізацією
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("user_id", "first_name", "last_name", "age", "is_seller")
    search_fields = ("user_id", "first_name", "last_name")
    ordering = ["user_id"]

    fieldsets = (
        (None, {"fields": ("user_id", "password", "email")}),
        ("Personal info", {"fields": ("first_name", "last_name", "age", "phone_number")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("user_id", "password1", "password2", "first_name", "last_name", "age"),
        }),
    )

# Реєструємо інші моделі
@admin.register(Talent_dsc)
class TalentDscAdmin(admin.ModelAdmin):
    list_display = ('id', 'prof')
    search_fields = ('prof',)

@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'position', 'location', 'talent_dsc')
    search_fields = ('user__user_id', 'position', 'location', 'talent_dsc__prof')
    list_filter = ('position', 'location')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date', 'status', 'user_id', 'location', 'created_at')
    search_fields = ('title', 'location', 'user_id__user_id')
    list_filter = ('status', 'location', 'start_date', 'end_date')

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'talent_id', 'project_id', 'price')
    search_fields = ('user_id__user_id', 'talent_id__position', 'project_id__title')
    list_filter = ('price',)
