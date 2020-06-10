# /accounts/urls.py
from django.conf.urls.static import static
from django.urls import path, include
from base import settings
from accounts.views import profile_view, guest_view, register_view, login_view, logout_view


app_name = 'accounts'

urlpatterns = [
    path('', profile_view, name="profile_view"),
    path('guest/', guest_view, name="guest_view"),
    path('profile/', profile_view, name="profile_view"),
    path('register/', register_view, name="register_view"),
    path('login/', login_view, name="login_view"),
    path('logout/', logout_view, name="logout_view"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
