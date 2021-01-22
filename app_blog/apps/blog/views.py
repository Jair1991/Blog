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
# #<!--17-->
from django.core.paginator import Paginator


# #<!--5-->
def index(request):
    # #<!--5-->
    # return HttpResponse("Hi world")
    # #<!--6-->
    # return render(request, "blog.html")
    # #<!--16 posts = Post.objects.all()--> # #<!--17-->
    list_posts = Post.objects.all()
    # #<!--17-->
    paginator = Paginator(list_posts, 3)
    # #<!--17-->
    page = request.GET.get("page") or 1
    # #<!--17-->
    posts = paginator.get_page(page)
    # #<!--17-->
    current_page = int(page)
    # #<!--17-->
    pages = range(1, posts.paginator.num_pages + 1)
    # #<!--16 return render(request, "blog.html", {"posts": posts})-->  # #<!--17-->
    return render(request, "blog.html", {"posts": posts, "pages": pages, "current_page": current_page})


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


# all config # #<!--18-->
def delete_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        messages.error(request, "The post to delete does not exist")
        return redirect("blog")

    if post.author != request.user:
        messages.error(request, "You are not the author of this post")
        return redirect("blog")

    post.delete()
    messages.success(request, F"The post {post.title} has been deleted")
    return redirect("blog")
