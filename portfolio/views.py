from django.shortcuts import render

# Create your views here.

def index(request):
	response = {

	}
	return render(request, 'portfolio.html', response)