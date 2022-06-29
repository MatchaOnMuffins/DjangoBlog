from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                path('', HomeView.as_view(), name='home'),
                path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
                path('post/new/', PostCreateView.as_view(), name='post_create'),
                path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
                path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
                path('post/<int:pk>/comment/new/', CommentCreateView.as_view(), name='comment_create'),
                path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_update'),
                path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
