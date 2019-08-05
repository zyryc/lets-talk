from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .forms import Postsform
from django.contrib import messages

from .models import Blog

def index(request):
	all_items = Blog.objects.order_by('-id', 'posts')
	if request.method == 'POST':
		form = Postsform(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ('post added'))
			return render(request, 'miniblog/index.html', {'all_items': all_items}) 
		else:
			return render(request, 'miniblog/index.html',  {'all_items': all_items})
	else:
		
		return render(request, 'miniblog/index.html', {'all_items': all_items})