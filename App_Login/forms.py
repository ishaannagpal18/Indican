from django.forms import ModelForm
from django import forms
from App_Login.models import UserProfile, Subscriber

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('email','username', 'password1', 'password2',)

class UserProfileChange(UserChangeForm):
    class Meta:
        model=User
        fields=('username', 'email', 'first_name', 'last_name', 'password')

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(

            Submit('submit', 'Subscribe', css_class='buton sbutton')
        )
