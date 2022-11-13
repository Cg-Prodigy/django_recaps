from django.contrib import admin

from .models import Landlord


# Register your models here.
@admin.register(Landlord)
class LandLordAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","middle_name","national_id","is_staff","is_superuser")
    fieldsets=(
        ("Personal",{"fields":("first_name","middle_name","last_name")}),
        ("Official",{"fields":("national_id","email")}),
        ("Others",{"fields":("is_staff","is_active","is_superuser")})
    )