from django.conf.urls.static import static
from django.urls import path, include
from base import settings
from .views import *


app_name = 'todo'

urlpatterns = [
    path('', home, name="todo_home"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
