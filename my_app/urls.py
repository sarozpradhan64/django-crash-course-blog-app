from django.urls import path 
from .views import home,blog,aboutUs,contactUs,blogDetail # . refers to current directory.

urlpatterns = [
    path('', home, name="home"),
    path('blog', blog, name="blog" ),
    path('blog/<int:blog_id>', blogDetail, name="blog-detail"),
    path('about', aboutUs, name="about-us"),
    path('contact-us', contactUs, name="contact-us")
]
