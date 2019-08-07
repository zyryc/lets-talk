from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import Postsform
from django.contrib import messages

from .models import Blog

def index(request):
	all_items = Blog.objects.order_by('-id', 'posts')
	return render(request, 'miniblog/index.html', {'all_items': all_items})
	
def add(request):
    if request.method == "POST":
    	form = Postsform(request.POST)
    	if form.is_valid():
    		Blog = form.save(commit=False)
    		Blog.save()
    		return render(request, 'miniblog/index.html', context_instance=RequestContext(request))

    	else:
    		return render(request, 'miniblog/add.html', {'form': form})
