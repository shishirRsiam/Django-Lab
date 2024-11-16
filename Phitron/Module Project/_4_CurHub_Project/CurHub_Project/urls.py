from django.contrib import admin
from django.urls import path
from . import views as Project_Views
from Authenticator_App import views as Authenticator_App_Views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Project_Views.home, name='home'), 

    path('view/info/', Project_Views.view_info, name='view_info'),

    path('profile/', Authenticator_App_Views.profile, name='profile'),
    path('edit/profile/', Authenticator_App_Views.edit_profile, name='edit_profile'),
    path('edit/password/', Authenticator_App_Views.change_password, name='change_password'),
    path('login/', Authenticator_App_Views.login_page, name='login'),
    path('logout/', Authenticator_App_Views.logout_page, name='logout'),
    path('signup/', Authenticator_App_Views.signup_page, name='signup'),
]
