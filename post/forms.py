from django import forms
from .models import post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

	class Meta:
		model=post
		fields=[
			'title',
			'content',
            'image',
			]
