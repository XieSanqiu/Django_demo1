from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth  #认证模块

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, "cookie_session_login.html")
    username = request.POST.get("username")
    password = request.POST.get("pwd")

    user_obj = auth.authenticate(username=username, password=password)
    print(user_obj.username)

    if not user_obj:
        return redirect("/CookieSession/login/")
    else:
        rep = redirect("/CookieSession/index/")
        rep.set_cookie("is_login", True)
        return rep


def index(request):
    print(request.COOKIES.get('is_login'))
    status = request.COOKIES.get('is_login')  # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    if not status:
        return redirect('/CookieSession/login/')
    return render(request, "cookie_session_index.html")


def logout(request):
    rep = redirect('/CookieSession/login/')
    rep.delete_cookie("is_login")
    return rep  # 点击注销后执行,删除cookie,不再保存用户状态，并弹到登录页面


def order(request):
    print(request.COOKIES.get('is_login'))
    status = request.COOKIES.get('is_login')
    if not status:
        return redirect('/CookieSession/login/')
    return render(request, "cookie_session_order.html")

def session_operation(request):
    request.session['sessionId'] = '12324323dfe343' # 存数据到session
    sessionId = request.session.get('sessionId')  # 从sessionId中取数据
    request.session.flush()  # 删除session
