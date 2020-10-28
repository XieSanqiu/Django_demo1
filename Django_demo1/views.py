from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from Django_demo1.my_forms import EmpForm, EmpForm2

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

def add_emp(request):
    if request.method == "GET":
        form = EmpForm()
        return render(request, "add_emp.html", {"form": form})
    else:
        form = EmpForm(request.POST)
        if form.is_valid():  # 进行数据校验
            # 校验成功
            data = form.cleaned_data  # 校验成功的值，会放在cleaned_data里。
            if 'r_salary' in data:
                data.pop('r_salary')
            print(data)

            return HttpResponse(
                'ok'
            )
            # return render(request, "add_emp.html", {"form": form})
        else:
            print(form.errors)    # 打印错误信息
            clean_errors = form.errors.get("__all__")
            print(222, clean_errors)
        return render(request, "add_emp.html", {"form": form, "clean_errors": clean_errors})

def add_emp2(request):
    if request.method == "GET":
        form = EmpForm2()  # 初始化form对象
        return render(request, "add_emp2.html", {"form":form})
    else:
        form = EmpForm2(request.POST)  # 将数据传给form对象
        if form.is_valid():  # 进行校验
            data = form.cleaned_data
            if 'r_salary' in data:
                data.pop('r_salary')
            # models.Emp.objects.create(**data)
            return redirect("/hello/")
        else:  # 校验失败
            clear_errors = form.errors.get("__all__")  # 获取全局钩子错误信息
            print('clear_errors:',clear_errors)
            print(form.errors)
            return render(request, "add_emp2.html", {"form": form, "clear_errors": clear_errors})