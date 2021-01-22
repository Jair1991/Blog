# all config # #<!--10-->
from django.db import models
from django.contrib.auth.models import User
# #<!--19-->
import os


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True, verbose_name='name')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True, null=False, verbose_name='Title')
    content = models.TextField(null=True, verbose_name='content the post')
    image = models.ImageField(upload_to='posts/%Y/%m/%d', null=True, blank=True, verbose_name='post image')
    high_date = models.DateTimeField(auto_now_add=True, verbose_name='High date')
    update_date = models.DateTimeField(auto_now_add=True, verbose_name='Update date')

    # #<!--19-->
    def delete(self, *args, **kwargs):
        # #<!--19-->
        if os.path.isfile(self.image.path):
            # #<!--19-->
            os.remove(self.image.path)
        # #<!--19 builder-->
        super(Post, self).delete(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']
