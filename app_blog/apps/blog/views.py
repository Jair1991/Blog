# #<!--1-->
from django.http import HttpResponse


# #<!--1-->
# def greeting(request):
# #<!--1-->
# return HttpResponse("Hi world")

# #<!--6--> # #<!--12-->
from django.shortcuts import render, redirect
# #<!--12-->
from apps.blog.forms import PostForms
# #<!--12-->
from django.contrib import messages
# #<!--16-->
from apps.blog.models import Post


# #<!--5-->
def index(request):
    # #<!--5-->
    # return HttpResponse("Hi world")
    # #<!--6-->
    # return render(request, "blog.html")
    # #<!--16-->
    posts = Post.objects.all()
    # #<!--16-->
    return render(request, "blog.html", {"posts": posts})


# all config # #<!--12-->
def create_post(request):

    if request.method == "POST":
        form = PostForms(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author_id = request.user.id
            post.save()
            title = form.cleaned_data.get("title")
            messages.success(request, f"{title} post is created correctly")
            return redirect("blog")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

    form = PostForms
    return render(request, "create_post.html", {"form": form})