import re
from django import forms
from .models import Tenant
from django.core.exceptions import ValidationError

def validatePassword(password):
    pattern=re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")
    if not re.search(pattern,password):
        return ValidationError("Weak password")
class TenantForm(forms.ModelForm):
    password=forms.CharField(max_length=30,widget=forms.PasswordInput(),validators=[validatePassword])
    c_password=forms.CharField(max_length=30,widget=forms.PasswordInput(),validators=[validatePassword])
    class Meta:
        model=Tenant
        fields=('first_name','last_name','email','id_no','password')

    def clean(self):
        data=super().clean()
        if data['password']!=data['c_password']:
            self.add_error('password','Passwords do not match')