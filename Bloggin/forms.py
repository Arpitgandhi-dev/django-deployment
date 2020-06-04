from django import forms
from django.contrib.auth.models import User
from Bloggin.models import UserProfileInfo, Blogdata

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email','password','first_name', 'last_name')


class UserBlogData(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')

class Bloggindata(forms.ModelForm):
    class Meta():
        model = Blogdata
        fields = ('Name', 'Blog')
    