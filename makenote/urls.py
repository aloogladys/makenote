
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from makenote_app.views import home,register,create,error,success,login, list_notes, delete_note, update_note, person




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('create/', create),
    path('list_notes/', list_notes, name='list_notes'),
    path('delete_note/<id>/', delete_note, name='delete_note'),
    path('update_note/<id>/', update_note, name="update_note"),
    path('login_page/', login, name = 'login'),
    path('register/', register),
    path('success/', success),
    path('error/', error),
    path('person/',person),
    path('', include('django.contrib.auth.urls')),

] + static(settings.MEDIA_URL,document_root=set)
