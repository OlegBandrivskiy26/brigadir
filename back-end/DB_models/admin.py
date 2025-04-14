from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Talent_dsc, Talent, Project, Contract

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "first_name", "last_name", "age", "is_seller")
    search_fields = ("email", "first_name", "last_name")
    ordering = ["email"]

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "age", "phone_number")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "first_name", "last_name", "age"),
        }),
    )

@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'position', 'location', 'talent_dsc')
    search_fields = ('user__email', 'position', 'location', 'talent_dsc__prof')
    list_filter = ('position', 'location', 'talent_dsc')

@admin.register(Talent_dsc)
class TalentDscAdmin(admin.ModelAdmin):
    list_display = ('id', 'prof')
    search_fields = ('prof',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date', 'status', 'user', 'location', 'created_at')
    search_fields = ('title', 'location', 'user__email')
    list_filter = ('status', 'location', 'start_date', 'end_date')

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'talent', 'project', 'price')
    search_fields = ('user__email', 'talent__position', 'project__title')
    list_filter = ('price',)
