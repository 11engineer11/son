from django import forms
from .models import HomePost


class HomeForm(forms.ModelForm):

	class Meta:
		model=HomePost
		fields=[
			'title',
            'user',
			'content',
            'image',
			]