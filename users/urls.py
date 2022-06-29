from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    # path('login/', Login.as_view(), name='login'),
    path('update_profile/', UpdateProfile.as_view(), name='update_profile'),
    path('password/', auth_views.PasswordChangeView.as_view(), name='password'),
    path('<int:pk>/profile/', ShowProfile.as_view(), name='self_profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
