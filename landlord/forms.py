from django import forms
from django.core.exceptions import ValidationError
from .models import Landlord
class LandlordSignUP(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Landlord
        fields=["first_name","middle_name","last_name","national_id","email","password"]
    def clean_national_id(self):
        data=self.cleaned_data['national_id']
        print(len(data),data,type(data))
        if len(data)!=8:
            raise ValidationError("Invalid ID number!")
        if data.isdigit()==False:
            raise ValidationError("ID should contain only digits")
        return data