from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from accounts.forms import CustomUserCreationForm, CustomSchoolCreationForm

# def index(request):
	# return render(request, 'accounts/index.html')


def register(request):
	if request.method == "GET":
		return render(request, "accounts/register.html", {"form": CustomUserCreationForm})
	elif request.method == "POST":
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect(reverse('login'))


def register_school(request):
	if request.method == "GET":
		return render(request, "accounts/register_school.html", {"form": CustomSchoolCreationForm})
	elif request.method == "POST":
		form = CustomSchoolCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect(reverse('login'))