from django.shortcuts import render,HttpResponse


def index(request):
    """
    首页
    :param request:
    :return:
    """
    return HttpResponse("欢迎来到首页")


def reg(request):
    """
    登陆
    :param request:
    :return:
    """

    return HttpResponse("登陆页面")

def add(request):
    """
    添加
    :param request:
    :return:
    """

    return HttpResponse("添加")

def bug(request):
    """
    bug
    :param request:
    :return:
    """

    return HttpResponse("bug")

def update(request):
    """
    更新功能
    :param request:
    :return:
    """
    return HttpResponse("更新功能")
