
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from makenote_app.views import main,home




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('home', home),
    


] + static(settings.MEDIA_URL,document_root=set)
