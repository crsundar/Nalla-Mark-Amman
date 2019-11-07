from django import forms

from .models import Post, Intense, Special


class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['name', 'town', 'city', 'state', 'phone', 'email', 'prayer', 'profile']


class IntenseForm(forms.ModelForm):

	class Meta:
		model = Intense
		fields = ['name', 'town', 'city', 'state', 'phone', 'email', 'prayer', 'profile']


class SpecialForm(forms.ModelForm):

	class Meta:
		model = Special
		fields = ['name', 'town', 'city', 'state', 'phone', 'email', 'prayer', 'profile']