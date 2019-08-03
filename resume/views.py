from django.shortcuts import render

# Create your views here.
	
mhs_name = 'Rully Fildansyah' 

def index(request):
	response = {
	'name': mhs_name,

	}
	return render(request, 'resume.html', response)