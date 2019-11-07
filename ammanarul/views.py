from django.shortcuts import render, redirect
from .models import *
from django.http import *
from .forms import *


def index(request):
	return render (request, 'ammanarul/index.html', {})


def choices(request):
	return render(request, 'ammanarul/choices.html', {})


def premium_list(request):
	posts = Post.objects.all()
	return render(request, 'ammanarul/premium_list.html', {'posts': posts})


def upload_premium(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('premium_list')
	else:
		form = PostForm()
	return render(request, 'ammanarul/upload_premium.html', {'form': form})


def intense_list(request):
	intense = Intense.objects.all()
	return render(request, 'ammanarul/intense_list.html', {'intense': intense})


def upload_intense(request):
	if request.method == "POST":
		form = IntenseForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('intense_list')
	else:
		form = IntenseForm()
	return render(request, 'ammanarul/upload_intense.html', {'form': form})


def special_list(request):
	special = Special.objects.all()
	return render(request, 'ammanarul/special_list.html', {'special': special})


def upload_special(request):
	if request.method == "POST":
		form = SpecialForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('special_list')
	else:
		form = SpecialForm()
	return render(request, 'ammanarul/upload_special.html', {'form': form})