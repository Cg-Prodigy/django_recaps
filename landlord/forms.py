import re
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .models import LandLord,House
class LandlordLogin(forms.Form):
    id_no=forms.CharField(label="National Id")
    password=forms.CharField(widget=forms.PasswordInput)
class LandLordForm(forms.ModelForm):
    pswd=forms.CharField(label="Password",widget=forms.PasswordInput)
    c_pswd=forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
    phone_number=forms.CharField(label="Primary phone number")
    class Meta:
        model=LandLord
        fields='__all__'
    def clean_phone_number(self):
        phone=self.cleaned_data['phone_number']
        regex=re.compile(r"^[0-9]{10}")
        if not regex.search(phone):
            raise ValidationError("Incorrect Phone number")
        return phone
    def clean_pswd(self):
        pswd=self.cleaned_data['pswd']
        regx=re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")
        if not regx.search(pswd):
            raise ValidationError(_("Password is weak!"))
        return pswd
    def clean_id_no(self):
        id_no=self.cleaned_data['id_no']
        regex=re.compile(r"^[0-9]{8}")
        if not regex.search(id_no):
            raise ValidationError(_("Invalid Id number."))
        return id_no
    def clean(self):
        data=super().clean()
        if data.get('pswd')!=data.get("c_pswd"):
            self.add_error('c_pswd','Passwords do not match.')
        print(data)

class HouseForm(forms.ModelForm):
    class Meta:
        model=House
        fields="__all__"