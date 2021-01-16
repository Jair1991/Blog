# #<!--2-->
# from django.shortcuts import render

# #<!--2-->
# def registry(request):
#   #<!--2-->
#   return render(request, "registry.html")
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm


# #<!--4 view-based class-->
class RecordView(View):
    # noinspection PyMethodMayBeStatic
    # used to display information <!--4-->
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registry.html", {"form": form})

    # noinspection PyMethodMayBeStatic
    # used to process information
    def post(self, request):
        pass
