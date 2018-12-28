from django.contrib import admin
from django.urls import path
from django.conf.urls import url

# from . import views
from .views import home_page, about_page, contact_page, login_page
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', home_page),
    url(r'about/$', about_page, name='about'),
    url(r'contact/$', contact_page, name='contactus'),
    url(r'login/$', login_page, name='login'),
]
