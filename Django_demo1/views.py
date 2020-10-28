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
            return render(request, 'success.html')
        else:
            url = reverse('reverse_login')
            return redirect(url)