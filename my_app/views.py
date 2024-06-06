from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog, ContactUs
from .forms import ContactUsForm
from django.urls import reverse

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
    blog = Blog.objects.filter(status = 'published', id=blog_id).first() #first() return single object.
    related_blogs = Blog.objects.filter(status = 'published').exclude(id = blog.id)


    return render(request, 'blog_detail.html', {"blog": blog, 'related_blogs': related_blogs})

def aboutUs(request):
    return render(request, 'about-us.html')


def contactUs(request):
    if request.method == "POST":
        form = ContactUsForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('home'))

        # full_name = request.POST.get('full_name')
        # email = request.POST.get('email')
        # mobile = request.POST.get('mobile')
        # message = request.POST.get('message')

        # if full_name and email and mobile and message:
        #     new_contact = ContactUs(full_name=full_name, email = email, mobile = mobile, message = message)
        #     new_contact.save()
        # else:
        #     return HttpResponse("<h1>Some value is missing</h1>")
    
    else:
        form = ContactUsForm()
    return render(request, 'contact-us.html', {'form':form})
