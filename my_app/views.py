from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

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
    
    books = [
        {"title": "Python Distilled", "author": "David M. Beazley", "year": 2021, "image": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSYckNTsPiXcSpBOYT7EhvgQKRT18gHNvhQ0c4WFB4POtzw7eOT"},
        {"title": "Fluent Python", "author": "Luciano Ramalho", "year": 2015, "image": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSHhzQJ0u-i63IdIfkFzMiUEt9yfKZ1GCjseF2H3vPYuBewOwF-"},
        {"title": "Automate the Boring Study", "author": "Al Sweigart", "year": 2019, "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqVjJPD-A1Sizgt6wKJMeEzLg8B33d_o5HeS4GA9aYbV8an7EF"},
    ]

    return render(request, 'index.html', {"title":title, "paragraph": paragraph, 'books':books})
    
def blog(request):
    return render(request, 'blog.html')

def aboutUs(request):
    return render(request, 'about-us.html')


def contactUs(request):
    return render(request, 'contact-us.html')