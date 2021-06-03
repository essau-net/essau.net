"""Users Forms"""

#Django
from django import forms

#local
from users.models import User


class SignupForm(forms.Form):
    """Sign up Form"""

    username = forms.CharField(min_length=1, max_length=30)
    
    email = forms.CharField(
        min_length=6,
        widget=forms.EmailInput(),
    )

    first_name = forms.CharField(
        min_length=2,
        max_length=150,
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=150,
    )

    password = forms.CharField(
        min_length=4,
        widget=forms.PasswordInput(),
    )
    password_confirmation = forms.CharField(
        min_length=4,
        widget=forms.PasswordInput(),
    )

    


    def clean_username(self):
        """Username must be unique"""
        username = self.cleaned_data['username']
        username_is_taken = User.objects.filter(username=username)
        print(f'\n\n\n clean_username \n\n\n')
        if username_is_taken:
            raise forms.ValidationError('Username is already in use')

        return username


    def clean_email(self):
        """Email must be unique"""

        email = self.cleaned_data['email']
        email_is_taken = User.objects.filter(email=email)
        print(f'\n\n\n clean_email \n\n\n')
        if email_is_taken:
            raise forms.ValidationError('Email is alredy in use')

        return email


    def clean(self):
        """Verify if passwords match"""

        data = super().clean()
        print(f'\n\n\n Dentro de clean {data} \n\n\n')
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match')

        return data

    def save(self):
        """Create the user"""

        data = self.cleaned_data
        data.pop('password_confirmation')

        User.objects.create_user(**data)