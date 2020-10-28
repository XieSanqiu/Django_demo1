from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

def hello_world(request):
    return HttpResponse('Hello World!')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if username == 'root' and pwd == '123':
            return render(request, 'success.html',{'username':username})
        else:
            url = reverse('reverse_login')
            return redirect(url)

def login2(request, year):
    print('year:',year)
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username2')
        pwd = request.POST.get('pwd2')
        if username == 'root' and pwd == '123':
            return render(request, 'success.html',{'username':username})
        else:
            url = reverse('reverse_login2', args=(2020,))
            return redirect(url)

def login3(request, year):
    print('year:',year)
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username2')
        pwd = request.POST.get('pwd2')
        if username == 'root' and pwd == '123':
            return render(request, 'success.html',{'username':username})
        else:
            url = reverse('reverse_login3', args=(2021,))
            return redirect(url)