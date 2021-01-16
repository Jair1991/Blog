# #<!--1-->
from django.urls import path
# #<!--1-->
from .views import greeting

# #<!--1-->
urlpatterns = [
    path('greeting/', greeting, name="greeting"),
]
