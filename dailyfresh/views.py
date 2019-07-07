from django.shortcuts import render, HttpResponse


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
