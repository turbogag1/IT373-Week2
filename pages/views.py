from django.shortcuts import render, get_object_or_404
from .models import Announcement

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

def announcements(request):
    announcements = Announcement.objects.all()
    return render(request, 'announcements.html', {'announcements': announcements})

def announcement_detail(request, id):
    announcements = get_object_or_404(Announcement, id=id)
    return render(request, 'announcement_detail.html', {'announcement': announcements})


def page_not_found_view(request, exception):
    return render(request, '404.html', status = 404)

def server_error_view(request):
    return render(request, '500.html', status = 500)