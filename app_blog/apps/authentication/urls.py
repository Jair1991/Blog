# #<!--2-->
# from django.urls import path
# #<!--2-->
# from .views import registry

# #<!--2-->
# urlpatterns = [
#    path('registry/', registry, name="registry"),
# ]

# #<!--4-->
from django.urls import path
# #<!--4-->
from .views import RecordView


# #<!--4-->
urlpatterns = [
    path('registry/', RecordView.as_view(), name="registry"),
]