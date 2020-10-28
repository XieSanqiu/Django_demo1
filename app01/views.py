from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

# Create your views here.

def hello_world(request):
    context = {}
    context['hello_world'] = 'Hello World!'
    context['list'] = ['list_0', 'list_1', 'list_2']
    context['dict'] = {'dict_name':'dict_value'}
    context['filter_safe'] = "<a href='https://www.baidu.com/'>点击跳转</a>"

    context['num'] = 80
    context['types'] = ('type1', 'type2', 'type3')

    context['student'] = {'name':'小明', 'age':12, '性别':'男'}

    context['letters'] = ["a", "b", "c", "d", "e"]

    return render(request, 'HelloWorld.html', context)

def extend(request):
    return render(request, 'child.html')

def static(request):
    return render(request, 'static.html')


def search(request):
    return render(request, 'form.html')

def search_get(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "form.html", ctx)

def index(request, year, month):
    print(year,month) # 一个形参代表路径中一个分组的内容，按关键字对应匹配
    return HttpResponse('菜鸟教程')

def date(request, year, month):
    print(year,month) # 一个形参代表路径中一个分组的内容，按关键字对应匹配
    date = '日期：'+ year + month
    return HttpResponse(date)

def login(request):
    print('命名空间')
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if username == 'root' and pwd == '123':
            return render(request, 'success.html',{'username':username})
        else:
            url = reverse('app01:reverse_login')
            return redirect(url)