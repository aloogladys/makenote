
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from makenote_app.views import home,register,create,error,success,login




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login_page/', login),
    path('register/', register),
    path('create/', create),
    path('success/', success),
    path('error/', error),
    path('', include('django.contrib.auth.urls')),
    
    
    


] + static(settings.MEDIA_URL,document_root=set)
