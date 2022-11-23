from django.contrib import admin
from .models import Tenant
# Register your models here.
@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','id_no','password']
    fieldsets=(
        ('Personal',{'fields':('first_name','last_name')}),
        ('Official',{'fields':('email','id_no')}),
        ('Auth',{'fields':('password',)})
    )