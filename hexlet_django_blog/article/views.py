from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


# def index(request):
#     return HttpResponse("asd")


def index(request):
    app_name = "articlesssssssssssss"
    return render(
        request,
        'articles/index.html',
        context={"app_name": app_name}
    )