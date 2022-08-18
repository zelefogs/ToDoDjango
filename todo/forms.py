from django.db import models
from django.forms import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, Textarea, TextInput, CheckboxInput
from .models import Todo


class TodoForm(ModelForm):
	class Meta:
		model = Todo
		fields = ['title', 'memo', 'important']
		widgets = {
			'title': TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Title'
			}),
			'memo': Textarea(attrs={
				'class': 'form-control mt-2',
				'placeholder': 'Description',
				'rows': '5'
			}),
			'important': CheckboxInput(attrs={
				'class': 'form-control-check mt-2 mb-2 p-1',
				'style': 'width: 20px; height: 20px'

			}),
		}
