from django import forms

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
    password=forms.CharField(widget=forms.PasswordInput)
    c_password=forms.CharField(widget=forms.PasswordInput)