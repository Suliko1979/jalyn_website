from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index_1', views.index_1, name='index_counter'),
    path('counter', views.counter, name='counter'),
    path('project', views.project_1, name='project'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('about', views.about, name='about'),
    path('post/<slug:pk>', views.post, name='post'),


]
