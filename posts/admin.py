from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Post

@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')
    ordering = ['-date']