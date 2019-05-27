from django.urls import path

from . import views

urlpatterns = [
    path('', views.gem_list, name='index'),
    path('random', views.gem_random, name='random'),
    path('<name>', views.gem_detail, name='detail'),
]
