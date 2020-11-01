from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

	class Meta:
		model = CustomUser
		fields = ('username', 'email')


class CustomSchoolCreationForm(UserCreationForm):
	last_name = forms.CharField(max_length=150, label='School name', required=True)
	is_teacher = forms.BooleanField(label='Registering as a school', required=True, initial=True)

	class Meta:
		model = CustomUser
		fields = ('username', 'last_name', 'email', 'is_teacher',)



class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = CustomUser
		fields = ('username', 'email')
