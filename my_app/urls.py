from django.urls import path 
from .views import home,blog,aboutUs,contactUs # . refers to current directory.

urlpatterns = [
    path('', home, name="home"),
    path('blog', blog, name="blog" ),
    path('about', aboutUs, name="about-us"),
    path('contact-message', contactUs, name="contact-us")
]
