from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
app_name = 'accounts'


urlpatterns = [
         # path('employeeregister/',views.employeeregistrationpage,name="employeeregistrationpage"),
         path('userregister/',views.userregistrationpage,name="userregistrationpage"),
         path('userlogin/',auth_views.LoginView.as_view(template_name='accounts/userloginpage.html'),name="userloginpage"),
         # path('userlogout/',auth_views.LogoutView.as_view(),name="userloginpage"),
    ]
