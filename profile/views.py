from django.shortcuts import render
from datetime import datetime, date

mhs_name = 'Rully Fildansyah'  
curr_year = int(datetime.now().strftime("%Y"))
birth_date = date(1998, 7, 11)  
departement = 'Teknik Informatika' 										
city = 'Sukabumi' 
phone = '+62 898 6431 126'
email = 'rullfhiel@gmail.com'														
interest = 'Web developer, IOT & Pythonista' 					
instagram = 'https://www.instagram.com/rvllfil/'						
github = 'https://github.com/rvllfil'									
linkedin = 'https://www.linkedin.com/in/rully-fildansyah-7a85b0168/'  	
twitter = 'https://twitter.com//rvllfil'								

# Create your views here.

def index(request):
    response = {
        'name': mhs_name,
        'age': calculate_age(birth_date.year),
        'birth_date': birth_date,
        'departement': departement,
        'city': city,
        'phone': phone,
        'email': email,
        'interest': interest,
        'instagram': instagram,
        'github': github,
        'linkedin': linkedin,
        'twitter': twitter
    }
    return render(request, 'index_profile.html', response)


def calculate_age(birth_year):
    return curr_year - birth_year if birth_year <= curr_year else 0
