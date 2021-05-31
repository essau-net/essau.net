"""Users Forms"""

#Django
from django import forms

#Users
from users.models import Users


class SignupForm(forms.Form):
    """Sign up Form"""

    username = forms.CharField(min_length=1, max_length=30)

    password = forms.CharField(
        widget=forms.PasswordInput(),
    )
    password_confirmation = forms.CharField(
        widget=forms.PasswordInput(),
    )

    permission_level = forms.CharField(max_length=9)

    url_profile_image = forms.URLField(max_length=250)


    def clean_username(self):
        """Username must be unique"""

        data = super().clean()

        username = self.cleaned_data['username']
        username_is_taken = Users.objects.filter(username=username)

        if username_is_taken:
            raise forms.ValidationError('Username is already in use')

        return data


    def clean(self):
        """Verify if passwords match"""

        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match')

        return data

    def save(self):
        """Create the user"""

        data = self.cleaned_data
        data.pop('password_confirmation')

        Users.objects.create_user(**data)