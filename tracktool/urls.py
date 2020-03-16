from django.urls import path
from . import views
app_name = 'accounts'
app_name='tracktool'
urlpatterns = [
    path('', views.home, name='home'),
    path('all_bugs', views.all_bugs, name='all_bugs'),
    path('my_bugs', views.my_bugs, name='my_bugs'),
    path('raise_bugs', views.raise_bugs, name='raise_bugs'),
    path('update_request/<int:pk>/edit/', views.update_request, name='update_request'),
    # path('delete_request/<int:pk>/delete/', views.delete_request, name='delete_request'),
]
