from django.contrib import admin
from django.contrib.admin import ModelAdmin

from . import models

# admin.site.register(models.Post)

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish', 'created', 'status']
    list_filter = ['author', 'status', 'publish', 'created']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author',]
    date_hierarchy = 'publish'
    ordering = ['-publish', 'status']

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created', 'post', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']

@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created', 'read']
    list_filter = ['read', 'created']
    search_fields = ['name', 'email', 'subject', 'message']

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'employer', 'language', 'preview', 'date']
    list_filter = ['employer', 'date', 'language']
    search_fields = ['title', 'employer', 'preview']