from django.urls import path
import store.views as views


urlpatterns = [
    path('', views.home, name='home'),
]
