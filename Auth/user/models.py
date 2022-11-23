from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.

class TenantManager(BaseUserManager):
    def create_user(self,first_name,last_name,email,id_no,password,**other_fields):
        self.normalize_email(email)
        user=self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            id_no=id_no,
            **other_fields,
        )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,first_name,last_name,email,id_no,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_active',True)
        other_fields.setdefault('is_superuser',True)
        return self.create_user(first_name,last_name,email,id_no,password,**other_fields)

class Tenant(AbstractBaseUser,PermissionsMixin):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    id_no=models.CharField(max_length=8,unique=True)
    # dob=models.DateField()
    objects=TenantManager()
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    USERNAME_FIELD='id_no'
    REQUIRED_FIELDS=['first_name','last_name','email']
