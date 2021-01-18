# #<!--2-->
# from django.shortcuts import render

# #<!--2-->
# def registry(request):
#   #<!--2-->
#   return render(request, "registry.html")
# #<!--5-->
from django.contrib import messages
# #<!--5--> # #<!--8--> # #<!--9-->
from django.contrib.auth import login, logout, authenticate
# #<!--5-->
from django.shortcuts import render, redirect
# #<!--4-->
from django.views.generic import View
# #<!--4--> # #<!--9-->
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# #<!--9 authenticate user-->
def accessing(request):
    # #<!--9-->
    if request.method == "POST":
        # #<!--9-->
        form = AuthenticationForm(request, data=request.POST)
        # #<!--9-->
        if form.is_valid():
            # #<!--9-->
            username = form.cleaned_data.get("username")
            # #<!--9-->
            password = form.cleaned_data.get("password")
            # #<!--9-->
            user = authenticate(username=username, password=password)
            # #<!--9-->
            if user is not None:
                # #<!--9-->
                login(request, user)
                # #<!--9-->
                messages.success(request, F"Welcome again {username}")
                # #<!--9-->
                return redirect("blog")
            # #<!--9-->
            else:
                # #<!--9-->
                messages.error(request, "The data is wrong")
        # #<!--9-->
        else:
            # #<!--9-->
            messages.error(request, "The data is wrong")
    # #<!--9-->
    form = AuthenticationForm()
    # #<!--9-->
    return render(request, "accessing.html", {"form": form})


# #<!--4 view-based class-->
class RecordView(View):
    # noinspection PyMethodMayBeStatic
    # used to display information <!--4-->
    def get(self, request):
        # #<!--4-->
        form = UserCreationForm()
        # #<!--4-->
        return render(request, "registry.html", {"form": form})

    # noinspection PyMethodMayBeStatic
    # used to process information
    # #<!--4-->
    def post(self, request):
        # #<!--4-->
        # pass
        # #<!--5-->
        form = UserCreationForm(request.POST)
        # #<!--5-->
        if form.is_valid():
            # #<!--5-->
            user = form.save()
            # #<!--5-->
            username = form.cleaned_data.get("username")
            # #<!--5-->
            messages.success(request, F"Welcome to the platform {username}")
            # #<!--5-->
            login(request, user)
            # #<!--5-->
            return redirect("blog")
        else:
            # #<!--5-->
            for msg in form.error_messages:
                # #<!--5-->
                messages.error(request, form.error_messages[msg])
            # #<!--5-->
            return render(request, "registry.html", {"form": form})


# #<!--8-->
def closed(request):
    # #<!--8-->
    logout(request)
    # #<!--8-->
    messages.success(request, F"Your session has been successfully closed")
    # #<!--8 return redirect("blog")--> # #<!--9-->
    return redirect("accessing")
