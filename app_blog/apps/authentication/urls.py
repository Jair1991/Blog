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
# #<!--4--> # #<!--8-->
from .views import RecordView, closed


# #<!--4-->
# #<!--8-->
urlpatterns = [
    path('registry/', RecordView.as_view(), name="registry"),
    path('closed/', closed, name="closed"),
]
