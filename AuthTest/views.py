from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth  #认证模块
from django.contrib.auth.models import User
import random
from django.contrib.auth.decorators import login_required

# Create your views here.

def create_user(request):
    User.objects.create(username='normal user1', password='xll123')  # 普通用户，密码不加密

    User.objects.create_user(username='normal user2', password='xll123')  # 普通用户，密码加密

    User.objects.create_superuser(username='super user', password='xll123', email='xll@123.com')  # 创建一个超级用户，密码是密文的，要多传一个邮箱 email 参数。

    return HttpResponse('创建用户成功！')

def auth_login(request):
    auth_code = generate_auth_code()
    if request.method == "GET":
        request.session['auth_code'] = auth_code
        print("auth_code",auth_code)
        return render(request, "auth_login.html", {'auth_code':auth_code})


    username = request.POST.get("username")
    password = request.POST.get("pwd")
    valid_num = request.POST.get("auth_code")
    keep_str = request.session.get("keep_str")
    auth_code = request.session.get('auth_code')
    print(keep_str, auth_code)
    print(valid_num, auth_code)
    if valid_num.upper() == auth_code.upper():
        user_obj = auth.authenticate(username=username, password=password)
        print(user_obj)
        if user_obj != None:
            print(user_obj.username)
            auth.login(request, user_obj)
            path = request.GET.get('next') or '/hello/'
            print(path)
            return redirect(path)
        else:
            return HttpResponse('用户名或密码错误')
    else:
        return HttpResponse('验证码错误')


def auth_logout(request):
    ppp = auth.logout(request)
    print(ppp) # None
    return redirect("/AuthTest/auth_login/")

@login_required
def login_required(request):
    return HttpResponse('已经登录')

def generate_auth_code():
    res = ''
    for i in range(6):
        a = random.randint(0, 99)
        if a < 26:
            res += chr(ord('A')+a)
        else:
            res += str(a % 10)
    return res

if __name__ == '__main__':
    print(generate_auth_code())