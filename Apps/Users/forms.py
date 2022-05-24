from dataclasses import field
from django import forms
from .models import Profile

class UserForm(forms.ModelForm):
    # def save(self, commit=True):
    #     user = super(UserForm, self).save(commit=False)
    #     user.set_password(self.cleaned_data['password'])
    #     user.is_active = True
    #     user.is_staff = False
    #     user.is_superuser = False
    #     if commit:
    #         user.save()
    #     return user

    
    class Meta:
        model = Profile
        # fields = ('__all__')
        fields = ('name','email','cpf',"password")