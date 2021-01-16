# #<!--1-->
from django.urls import path
# #<!--1-->
# from .views import greeting

# #<!--1-->
# urlpatterns = [
# path('greeting/', index, name="greeting"),
# ]
# #<!--5-->
from apps.blog.views import index

# #<!--5-->
urlpatterns = [
    path('', index, name="blog"),
]