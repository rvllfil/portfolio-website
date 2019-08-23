from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    response = {}
    # user = None
    if request.method == "POST":
        user_login = request.POST['username']
        pass_login = request.POST['password']

        user = authenticate(request, username=user_login, password=pass_login)
        print(user)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('login')
    html = 'login.html'
    return render(request, html, response)

def logout_view(request):
    response = {}

    if request.method == "POST":
        print(request.POST)
        if request.POST["logout"] == "Submit Query":
            logout(request)
        return HttpResponseRedirect('/')

    return render(request, 'logout.html', response)


def inici(request):
    zones = Zona.objects.all()
    return render_to_response('layout/base.html', dict(zones=zones),
        context_instance = RequestContext(request))