from django.urls import path
from . import views
app_name = 'Home'

urlpatterns = [
    path('', views.home, name="index"),
    path('india/', views.india, name="india"),
    path('world/', views.world, name="world"),
    path('entertainment/', views.entertainment, name="entertainment"),
    path('life_style/', views.life_style, name="life_style"),
    path('sports/', views.sports, name="sports"),
    path('Technology/', views.technology, name="technology"),
    path('business/', views.business, name="business")
]
