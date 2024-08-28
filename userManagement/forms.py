from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from userManagement.models import Department, HeaderSettings

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True,
                         label='Email',
                         error_messages={'exists': 'Oops'})

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name")


    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        exclude = ('users', )
        widgets = {
            'admin': forms.HiddenInput
        }


class HeaderSettingsForm(forms.ModelForm):
    class Meta:
        model = HeaderSettings
        fields = '__all__'
        exclude = ('user', )