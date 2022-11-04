from django.db import models

# Create your models here.
class LandLord(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email_address=models.EmailField()
    id_no=models.CharField(unique=True,max_length=8)
    phone_number=models.CharField(max_length=10)
    pswd=models.CharField(max_length=20)
    c_pswd=models.CharField(max_length=20)
class House(models.Model):
    class HType(models.TextChoices):
        BD="BD","Bed seater"
        OB="OB","One Bedroom"
    house_name=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    h_type=models.CharField(max_length=15,choices=HType.choices)
    landlord=models.ForeignKey(LandLord,on_delete=models.CASCADE)