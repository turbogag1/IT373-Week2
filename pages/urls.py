from django.urls import path, include
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('hello/<str:name>/', views.hello, name='hello'),
    path('gallery/', views.gallery, name='gallery'),
    path('announcements/', views.announcements, name='announcements'),
    path('announcements/<int:id>/', views.announcement_detail, name='announcement_detail'),
]