from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse  # 从http模块中导入HttpResponse类


# Create your views here.
def index(request):  # 定义站点首页视图函数
    return HttpResponse('啊！~~这是我的第一次！')  # 返回响应内容对象