from django.shortcuts import render,HttpResponse


def index(request):
    """
    首页
    :param request:
    :return:
    """
    return HttpResponse("欢迎来到首页")


