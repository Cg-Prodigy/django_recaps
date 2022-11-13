from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.
class LandlordManager(BaseUserManager):
    def create_user(self,first_name,middle_name,last_name,email,national_id,password,**other_fields):
        email=self.normalize_email(email)
        user=self.model(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            email=email,
            national_id=national_id,
            **other_fields,
        )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,first_name,middle_name,last_name,email,national_id,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_active',True)
        other_fields.setdefault('is_superuser',True)
        return self.create_user(first_name,middle_name,last_name,email,national_id,password,**other_fields)
class Landlord(AbstractBaseUser,PermissionsMixin):
    first_name=models.CharField(max_length=20)
    middle_name=models.CharField(max_length=20,blank=True)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    national_id=models.CharField(max_length=8,unique=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    objects=LandlordManager()
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["first_name","last_name","middle_name","national_id"]

    def __str__(self) -> str:
        return self.first_name+ " "+self.last_name