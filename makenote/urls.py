
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from makenote_app.views import home,register,login,create,error,success




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', login),
    path('register/', register),
    path('create/', create),
    path('success/', success),
    path('error/', error),
    
    


] + static(settings.MEDIA_URL,document_root=set)
