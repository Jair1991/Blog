# #<!--2-->
from django.urls import path
# #<!--2-->
from .views import registry

# #<!--2-->
urlpatterns = [
    path('registry/', registry, name="registry"),
]
