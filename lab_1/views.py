from django.shortcuts import render
from datetime import datetime, date
# Enter your name here
mhs_name = 'Rully Fildansyah'  # TODO Implement this
curr_year = int(datetime.now().strftime("%Y"))
birth_date = date(1998, 7, 11)  # TODO Implement this, format (Year, Month, Date)
departement = 'Teknik Informatika' 										# TODO Implement this
city = 'Sukabumi' 														# TODO Implement this
interest = 'Web, IOT, dan Bahasa Python (Pythonista).' 					# TODO Implement this
instagram = 'https://www.instagram.com/rvllfil/'						# TODO Implement this
github = 'https://github.com/rvllfil'									# TODO Implement this
linkedin = 'https://www.linkedin.com/in/rully-fildansyah-7a85b0168/'  	# TODO Implement this
twitter = 'https://twitter.com//rvllfil'								# TODO Implement this

# Create your views here.


def index(request):
    response = {
        'name': mhs_name,
        'age': calculate_age(birth_date.year),
        'birth_date': birth_date,
        'departement': departement,
        'city': city,
        'interest': interest,
        'instagram': instagram,
        'github': github,
        'linkedin': linkedin,
        'twitter': twitter
    }
    return render(request, 'index_lab1.html', response)


def calculate_age(birth_year):
    return curr_year - birth_year if birth_year <= curr_year else 0
