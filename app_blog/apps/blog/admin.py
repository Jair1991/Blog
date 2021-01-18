# #<!--14-->
from django.contrib import admin
# #<!--14-->
from apps.blog.models import Category, Post

# #<!--14-->
admin.site.register([Category, Post])

