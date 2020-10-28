from django.shortcuts import render, HttpResponse, redirect
from TestModel.models import Test

# Create your views here.
def test_db_add(request):
    test1 = Test(name='小明', age=12)
    test1.save()
    test2 = Test(name='小华', age=15)
    test2.save()
    return HttpResponse('添加数据成功！')

def test_db_query(request):
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    result1 = Test.objects.all()
    for p in result1:
        print(p)

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    result2 = Test.objects.filter(name='小明')
    print(result2)

    # 获取单个对象
    result3 = Test.objects.get(id=1)
    print(result3)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    result4 = Test.objects.order_by('age')[0:2]
    print(result4)

    # 上面的方法可以连锁使用
    result5 = Test.objects.filter(name="小明").order_by("id")
    print(result5)

    return HttpResponse('查询成功')

def test_db_update(request):
    # 修改其中一个id=1的字段，再save，相当于SQL中的UPDATE
    test1 = Test.objects.get(id=2)
    test1.name = '小丽'
    test1.age = 13
    test1.save()

    # 另外一种方式
    # Test.objects.filter(id=2).update(name='小丽', age=13)

    # 修改所有的列
    # Test.objects.all().update(name='Google')

    return HttpResponse("<p>修改成功</p>")

def test_db_delete(request):
    # 删除id=1的数据
    test1 = Test.objects.get(id=1)
    test1.delete()

    # 另外一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    # Test.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")