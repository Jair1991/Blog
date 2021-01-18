# #<!--1-->
from django.http import HttpResponse


# #<!--1-->
# def greeting(request):
# #<!--1-->
# return HttpResponse("Hi world")

# #<!--6-->
from django.shortcuts import render


# #<!--5-->
def index(request):
    # #<!--5-->
    # return HttpResponse("Hi world")
    # #<!--6-->
    return render(request, "blog.html")
