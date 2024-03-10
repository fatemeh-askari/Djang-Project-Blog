from django.urls import path
from . import views

app_name = 'blogapp'

urlpatterns = [
    path('services/', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('', views.home, name='home'),
    # path('post/<slug:slug>/comments/', views.post_comment, name='post_comment')
    # path('success/', views.success_url, name='success_url'),
    path('contact/', views.contact_us, name='contact_us'),
    path('blog/', views.blog, name='blog'),
    path('projects/', views.project, name='projects')
]
