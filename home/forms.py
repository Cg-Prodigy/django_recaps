import re
from django import forms
from django.core.exceptions import ValidationError

# custom validators
def validate_password(value):
    regx=re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")
    if not re.search(regx,value):
        raise ValidationError("Password is weak!")


class LoginForm(forms.Form):
    CAREER_CHOICES=(
        ('Computer Science',
        (('DS','Data Science'),
        ("DO","DevOps"),
        ("WD","Web Development"))
        ),
        ("Management",
        (("DM","Database Management"),
        ("HR","Human Resource"))
        )
    )
    GENDER=(
        ("Male","Male"),
        ("Female","Female"),
        ("Choose not to say","Choose not to say")
    )
    first_name=forms.CharField()
    last_name=forms.CharField()
    email_address=forms.EmailField()
    dob=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender=forms.ChoiceField(choices=GENDER,widget=forms.RadioSelect)
    main_career=forms.ChoiceField(choices=CAREER_CHOICES)
    sub_careers=forms.MultipleChoiceField(choices=CAREER_CHOICES)
    years_of_experience=forms.IntegerField()
    about_yourself=forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Create a strong password."}), validators=[validate_password],
    help_text="""
    <ul>
    <li>Should have at least one number.</li>
    <li>Should have at least one uppercase and one lowercase character.</li>
    <li>Should have at least one special symbol.</li>
    <li>Should be between 6 to 20 characters long.</li>
    </ul>"""
    )
    c_password=forms.CharField(widget=forms.PasswordInput,validators=[validate_password])
    def clean_first_name(self):
        value=self.cleaned_data['first_name'].strip()
        return value.title()
    def clean(self):
        data=super().clean()
        if data.get('password')!=data.get('c_password'):
            self.add_error('c_password',"Passwords do not match!")