from django.urls import path
from . import views
app_name = 'tracktool'
urlpatterns = [
    path('home', views.home, name='home'),
    path('all_bugs', views.all_bugs, name='all_bugs'),
    path('raise_bugs', views.raise_bugs, name='raise_bugs'),
    path('update_request/<int:pk>/edit/', views.update_bugs, name='update_request'),
]
