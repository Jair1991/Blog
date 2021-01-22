# #<!--1-->
from django.urls import path
# #<!--1-->
# from .views import greeting

# #<!--1-->
# urlpatterns = [
# path('greeting/', index, name="greeting"),
# ]
# #<!--5--> # #<!--12-->  # #<!--18-->
from apps.blog.views import index, create_post, delete_post

# #<!--5--> # #<!--12--> # #<!--18 pass parameter->
urlpatterns = [
    path('', index, name="blog"),
    path('post/create', create_post, name="create_post"),
    path('post/delete/<int:post_id>', delete_post, name="delete_post"),
]
