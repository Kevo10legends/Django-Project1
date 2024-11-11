from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name='my_home'),
    path('about',views.about,name='my_about'),
    path('login',views.login,name='my_login'),
    path('offers',views.service,name='my_services'),
    path('contact',views.contact,name='my_contact'),
    path('blog',views.blog,name='my_blog'),
    path('new',views.new,name='my_new'),


]