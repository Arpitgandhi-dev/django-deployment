from django.conf.urls import url
from Bloggin import views

app_name = 'Bloggin'

urlpatterns  = [
    url(r'^register/$', views.register, name= 'register'),
    url(r'^user_login/$', views.user_login, name = 'user_login'),
    url(r'^bloger/$', views.Bloggerfunc, name= 'Bloggerfunc')
   
]