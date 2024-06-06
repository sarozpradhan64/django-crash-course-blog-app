from django.contrib import admin
from .models import Blog, ContactUs


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'is_featured', 'status', 'publish_date']
    list_filter = ['publish_date']
    search_fields = ['title', 'author']

admin.site.register(Blog, BlogAdmin) #register Blog model in admin.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'mobile', 'message']

admin.site.register(ContactUs, ContactAdmin)