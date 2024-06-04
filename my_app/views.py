from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

def home(request):
    title = "Django Blog App!"

    paragraph = """Lorem Ipsum is simply dummy text of the printing and typesetting 
    industry.Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
    when an unknown printer took a galley of type and scrambled it to make a type 
    specimen book. It has survived not only five centuries, but also the leap into 
    electronic typesetting, remaining essentially unchanged. It was popularised in the
      1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more 
      recently with desktop publishing software like Aldus PageMaker including versions of
        Lorem Ipsum."""
    # blogs = Blog.objects.all()
    featured_blogs = Blog.objects.filter(status="published", is_featured = True)
    return render(request, 'index.html', {"title":title, "paragraph": paragraph, 'featured_blogs': featured_blogs })
    
def blog(request):
    title = "My blog"
    paragraph = "Please read my blogs, all of those are intresting ones."

    blogs = Blog.objects.filter(status = "published")
    return render(request, 'blog.html', {'title':title, 'paragraph': paragraph, 'blogs' : blogs })


def blogDetail(request, blog_id):
    blog = Blog.objects.filter(id=blog_id).first()
    return render(request, 'blog_detail.html', {"blog": blog})

def aboutUs(request):
    return render(request, 'about-us.html')


def contactUs(request):
    return render(request, 'contact-us.html')