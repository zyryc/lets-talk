from django import forms
from .models import Blog

class Postsform(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ('posts', 'file_name',)