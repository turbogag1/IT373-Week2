from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title': 'Home', 
        'features': [
            'Django', 
            'Templates', 
            'Static Files'
        ]
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {'title': 'About'})

def hello(request, name):
    return render(request, 'hello.html', {'name': name})

def gallery(request):
    # assume images placed in pages/static/img
    images = ['img1.jpg', 'img2.jpg', 'img3.jpg']
    return render(request, 'gallery.html', {'images': images})