from django import forms


class UsersForm(forms.Form):
    UserName = forms.CharField(label="User Name")
    E_mail = forms.EmailField(label="E-mail")
    Password = forms.CharField(label="Password", widget=forms.PasswordInput)
    Birthdate = forms.DateField(label="Birthdate")
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    Gender = forms.ChoiceField(label="Gender", choices=GENDER_CHOICES)
    


