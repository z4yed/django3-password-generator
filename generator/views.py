from django.shortcuts import render
import random

# Create your views here.

def home(request):
	return render(request, 'generator/home.html')

def password(request):

	generated_password = ''

	characters = list('abcdefghijklmnopqrstuvwxyz')
	length = int(request.GET.get('length'))

	if request.GET.get('uppercase'):
		characters.extend("ABCDEFGHIJKLMNOPQURSTUVWXYZ")

	if request.GET.get('number'):
		characters.extend("1234567890")

	if request.GET.get('special'):
		characters.extend("!@#$%^&()*)_")

	for _ in range(length):
		generated_password += random.choice(characters)


	return render(request, 'generator/password.html', {'password' : generated_password})


def about(request):
	return render(request, 'generator/about.html')