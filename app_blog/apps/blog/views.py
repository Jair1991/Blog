# #<!--1-->
from django.http import HttpResponse


# #<!--1-->
def greeting(request):
    # #<!--1-->
    return HttpResponse("Hi world")
