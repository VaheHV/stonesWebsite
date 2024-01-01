from django.urls import path
from . import views

# Serving media files during development
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('product/', views.products, name='products'),
    path('about/', views.about, name='about'),
    path('blog/<int:pk>/', views.article_page, name='article'),
    path('product/<int:pk>/', views.product_page, name='product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
